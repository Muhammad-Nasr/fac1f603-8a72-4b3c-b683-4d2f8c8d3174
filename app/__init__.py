# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import config_dict

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please log in to access this page.'
migrate = Migrate()


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_class])
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    from app.authentication import bp as auth_bp
    app.register_blueprint(auth_bp)
    from app.home import bp as home_bp
    app.register_blueprint(home_bp)

    return app






