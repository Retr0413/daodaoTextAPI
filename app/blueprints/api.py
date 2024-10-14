from flask import request, jsonify
from flask_restful import Api, Resource
from app.models import db, Text
import os

UPLOAD_FOLDER = 'app/uploads'

class UploadPDF(Resource):
    def post(self):
        pdf = request.files.get('file')
        name = request.form.get('name')
        title = request.form.get('title')
        body = request.form.get('body')
        tags = request.form.get('tags', '')  

        if not pdf or not name or not title or not body:
            return jsonify({'error': "Missing required fields"}), 400

        filepath = os.path.join(UPLOAD_FOLDER, pdf.filename)
        pdf.save(filepath)

        new_text = Text(
            name=name,
            title=title,
            body=body,
            tags=tags,
            pdf_path=filepath
        )
        db.session.add(new_text)
        db.session.commit()

        return jsonify({'message': 'PDF uploaded successfully'})

class GetLabels(Resource):
    def get(self):
        texts = Text.query.all()
        return jsonify([text.serialize() for text in texts])

class ProcessJSON(Resource):
    def post(self):
        data = request.json

        if not data or 'name' not in data or 'title' not in data or 'body' not in data:
            return jsonify({'error': 'Invalid JSON'}), 400

        new_text = Text(
            name=data['name'],
            title=data['title'],
            body=data['body'],
            tags=data.get('tags', ''),
            pdf_path=data.get('pdf_path', '')
        )
        db.session.add(new_text)
        db.session.commit()

        return jsonify({'message': 'JSON processed successfully'})

def create_api(app):
    api = Api(app)
    api.add_resource(UploadPDF, '/api/upload')
    api.add_resource(GetLabels, '/api/labels')
    api.add_resource(ProcessJSON, '/api/process')
