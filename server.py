import os

from app.core import create_app, db
from flask_migrate import Migrate
from app import blueprint

# import models for migrate
from app.core.models import *

app = create_app(os.getenv('FLASK_ENV') or 'develop')
app.register_blueprint(blueprint)
migrate = Migrate(app, db)
