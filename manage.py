from app import create_app
from app.extensions import db
from app.models import Text
import os

app = create_app()

with app.app_context():
    pdf_path = '/app/uploads/robothand.pdf'

    new_text = Text(
        name='Robot Hand',
        title='The Future of Robotics',
        thumbnail=None,  
        description='A detailed analysis on robotic hands',
        body='This is the body of the PDF.',
        tags='robotics, AI',
        is_public=True,
        pdf_path=pdf_path
    )

    db.session.add(new_text)
    db.session.commit()

    print(f"Text '{new_text.title}' added with ID {new_text.id}.")
