def test_text_model(app):
    from app.models import Text

    text = Text(
        name='test-text',
        title='Test Text',
        body='This is a test body.',
        is_public=True
    )

    assert text.name == 'test-text'
    assert text.title == 'Test Text'
    assert text.body == 'This is a test body.'
    assert text.is_public is True
