from flask_restx import Api
from flask import Blueprint

from .core.resources.user_resource import api as user_ns
from .core.resources.board_resource import api as board_ns
from .core.resources.article_resource import api as article_ns
from .core.resources.auth_resource import api as auth_ns
from .core.resources.dashboard_resource import api as dashboard_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='Flask project sample',
    version='0.1.0',
    description='Flask with flask-restx',
    doc='/doc/'
)

api.add_namespace(user_ns, path='/users')
api.add_namespace(board_ns, path='/boards')
api.add_namespace(article_ns, path='/articles')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(dashboard_ns, path='/dashboard')
