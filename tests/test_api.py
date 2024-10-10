import os

def tesst_upload_pdf(client):
    pdf_path = 'test.pdf'
    with open(pdf_path, 'wb') as f:
        f.write(b'%PDF-1.7\n')

    data = {
        'name': 'test',
        'title': 'test',
        'body': 'test',
        'tags': 'test',
        'is_public': True,
        'description': 'test'
    }
    with open(pdf_path, 'rb') as pdf_file:
        response = client.post('/api/upload_pdf', data=data, content_type='multipart/form-data', files={'pdf_file': pdf_file})

    assert response.status_code == 201
    assert 'id' in response.get_json()

    os.remove(pdf_path)

def test_cors_headers(client):
    response = client.get('/api/texts')

    assert response.status_code == 200

    assert 'Access-Control-Allow-Origin' in response.headers
    assert response.headers['Access-Control-Allow-Origin'] == '*'