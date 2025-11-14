import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = os.path.join('SECRET_KEY') or 'super-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///assignments.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
