from flask import Flask, render_template, request
from app.config import Config
from app.extensions import db, migrate, login_manager
from app import public, user, post
from app.user.models import User
from flask_login import current_user

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    register_extensions(app)

    register_blueprint(app)
    
    return app

def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    register_login_manager(app)


def register_login_manager(app):
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
    
    @app.context_processor
    def inject_user():
        return dict(user=current_user)



def register_blueprint(app: Flask):
    app.register_blueprint(public.views.blueprint)
    app.register_blueprint(user.views.blueprint)
    app.register_blueprint(post.views.blueprint)





