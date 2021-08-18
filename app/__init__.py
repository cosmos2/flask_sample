from flask_restx import Api
from flask import Blueprint

from .core.resources.user_resource import api as user_ns
from .core.resources.board_resource import api as board_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Flask project sample',
    version='0.1.0',
    description='Flask with flask-restx',
)

api.add_namespace(user_ns, path='/users')
api.add_namespace(board_ns, path='/boards')
