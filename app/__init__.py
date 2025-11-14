from app.extenshions import *
from flask import Flask
import os
from config import Config
from app.models import User
from flask_login import current_user

def create_app():
    app = Flask(__name__, template_folder=os.path.abspath('templates'))
    app.config.from_object(Config)

    # ==============================
    # FILE UPLOAD CONFIG
    # ==============================
    upload_path = os.path.join(os.getcwd(), 'uploads')
    os.makedirs(upload_path, exist_ok=True)
    app.config['UPLOAD_FOLDER'] = upload_path

    # ==============================
    # DATABASE
    # ==============================
    db.init_app(app)

    @login_manager.user_loader
    def user_loader(user_id):
        return User.query.get(int(user_id))
    
    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # ==============================
    # ROUTES
    # ==============================
    from app.routes.auth import auth
    from app.routes.routes import main

    app.register_blueprint(auth)
    app.register_blueprint(main)

    # ==============================
    # CREATE TABLES
    # ==============================
    with app.app_context():
        db.create_all()

    return app
