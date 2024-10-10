from flask import Blueprint, request, jsonify, current_app
import os
from werkzeug.utils import secure_filename
from .models import Text
from .extensions import db

routes = Blueprint('routes', __name__)

# PDFファイルのアップロード
@routes.route('/upload_pdf', methods=['POST'])
def upload_pdf():
    file = request.files.get('pdf_file')
    name = request.form.get('name')
    title = request.form.get('title')
    body = request.form.get('body')
    tags = request.form.get('tags')
    is_public = request.form.get('is_public', True)
    description = request.form.get('description', '')

    if not file or not file.filename.endwith('.pdf'):
        return jsonify({'message': 'Invalid PDF file'}), 400
    
    filename = secure_filename(file.filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)

    new_text = Text(
        name=name,
        title=title,
        body=body,
        tags=tags,
        is_public=is_public,
        description=description,
        pdf_path=file_path
    )
    db.session.add(new_text)
    db.session.commit()

    return jsonify({'message': 'PDF uploaded successfully', 'id': new_text.id}), 201

# 教科書データの取得
@routes.route('/texts', methods=['GET'])
def get_texts():
    texts = Text.query.all()
    return jsonify([text.serialize() for text in texts]), 200