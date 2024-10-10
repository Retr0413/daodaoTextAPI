from .extensions import db

class Text(db.Model):
    __tablename__ = 'texts'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
    name = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    thumbnail = db.Column(db.String(255))
    description = db.Column(db.Text)
    body = db.Column(db.Text, nullable=False)
    tags = db.Column(db.String(255))
    is_public = db.Column(db.Boolean, default=True, nullable=False)
    pdf_path = db.Column(db.String(255))

    def serialize(self):
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'name': self.name,
            'title': self.title,
            'thumbnail': self.thumbnail,
            'description': self.description,
            'body': self.body,
            'tags': self.tags,
            'is_public': self.is_public,
            'pdf_path': self.pdf_path
        }