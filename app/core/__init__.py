from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

from .config import config_by_name

# extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
cors = CORS()
session = Session()
ma = Marshmallow()
login_manager = LoginManager()
cache = Cache()


def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    db.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
    session.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)
    cache.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.query.get(int(user_id))

    return app
