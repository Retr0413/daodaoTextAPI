import json
import os

def test_upload_pdf(client):
    data = {
        'file': (open('app/uploads/robothand.pdf', 'rb'), 'robothand.pdf'),
        'label': 'Sample PDF'
    }
    response = client.post('/api/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert response.get_json() == {"message": "PDF uploaded successfully"}

def test_get_labels(client):
    response = client.get('/api/labels')
    assert response.status_code == 200
    labels = response.get_json()
    assert isinstance(labels, list)
    if labels:
        assert "name" in labels[0]
        assert "title" in labels[0]

def test_process_json(client):
    data = {
        'name': 'test-name',
        'title': 'test-title',
        'body': 'test-body',
        'tags': 'test-tag'
    }
    response = client.post('/api/process', data=json.dumps(data), content_type='application/json')
    assert response.status_code == 200
    assert response.get_json() == {"message": "JSON processed successfully"}

    response = client.get('/api/labels')
    labels = response.get_json()
    assert any(label['name'] == 'test-name' and label['title'] == 'test-title' for label in labels)
