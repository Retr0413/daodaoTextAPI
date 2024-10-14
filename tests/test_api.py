import json
import os

def test_upload_pdf(client):
    data = {
        'file': (open('app/uploads/robothand.pdf', 'rb'), 'robothand.pdf'),
        'label': 'Sample PDF'
    }
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert response.get_json() == {"message": "PDF uploaded and labeled successfully."}

def test_get_labels(client):
    response = client.get('/labels')
    assert response.status_code == 200
    labels = response.get_json()
    assert isinstance(labels, list)
    if labels:
        assert "filename" in labels[0]
        assert "label" in labels[0]

def test_process_json(client):
    data = {'filename': 'test.pdf', 'label': 'Test Label'}
    response = client.post('/process', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.get_json() == {"message": "JSON processed and labeled successfully."}

    response = client.get('/labels')
    labels = response.get_json()
    assert any(label['filename'] == 'test.pdf' and label['label'] == 'Test Label' for label in labels)