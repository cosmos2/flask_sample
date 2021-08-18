from flask import Flask
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name

# extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
cors = CORS()
session = Session()
ma = Marshmallow()


def create_app(config_name: str):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    
    db.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)
    session.init_app(app)
    ma.init_app(app)

    return app
