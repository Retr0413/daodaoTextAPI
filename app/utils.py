import os

def allowed_file(filename):
    from .config import Config
    return '.' in filename and \
              filename.rsplit('.', 1)[1].lower() in Config.ALLOWED_EXTENSIONS