from flask import request, jsonify, send_from_directory, current_app
import os
from werkzeug.utils import secure_filename
from . import api_blueprint
from ..models import Text
from ..extensions import db
from ..utils import allowed_file

@api_blueprint.route('/api/texts', methods=['POST'])
def create_text():
    data = request.form.to_dict()
    file = request.files.get('pdf_file')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = current_app.config['UPLOAD_FOLDER']
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file.save(os.path.join(upload_folder, filename))
        pdf_path = os.path.join(upload_folder, filename)
    else:
        pdf_path = None

    text = Text(
        name=data['name'],
        title=data['title'],
        thumbnail=data.get('thumbnail'),
        description=data.get('description'),  # typo: 'defcription' -> 'description'
        body=data['body'],
        tags=data.get('tags'),
        is_public=data.get('is_public', True),
        pdf_path=pdf_path
    )
    db.session.add(text)
    db.session.commit()
    return jsonify({'message': 'Text created successfully', 'id': text.id}), 201

@api_blueprint.route('/api/texts/<int:id>', methods=['GET'])
def get_text(id):
    text = Text.query.get_or_404(id)
    return jsonify(text.serialize())

@api_blueprint.route('/api/texts/<int:id>/download', methods=['GET'])
def download_pdf(id):
    text = Text.query.get_or_404(id)
    if text.pdf_path and os.path.exists(text.pdf_path):
        directory = os.path.dirname(text.pdf_path)
        filename = os.path.basename(text.pdf_path)
        return send_from_directory(directory, filename, as_attachment=True)
    else:
        return jsonify({'message': 'PDF file not found'}), 404
