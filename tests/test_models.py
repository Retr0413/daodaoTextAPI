def test_text_model(app):
    from app.models import Text

    text = Text(
        name='test-text',
        title='Test Text',
        body='This is a test body.',
        tags='sample tag',
        pdf_path='/path/to/sample.pdf'
    )

    assert text.name == 'test-text'
    assert text.title == 'Test Text'
    assert text.body == 'This is a test body.'
    assert text.tags == 'sample tag'
    assert text.pdf_path == '/path/to/sample.pdf'