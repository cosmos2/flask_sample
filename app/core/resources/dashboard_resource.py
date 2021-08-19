from flask_login import login_required
from flask_restx import Resource, Namespace

from app.core import cache
from app.core.models import Board, dashboard_schema

api = Namespace('dashbaord', description='대쉬보드')


@api.route('/')
class DashboardList(Resource):

    @login_required
    @cache.cached(timeout=60 * 15)
    def get(self):
        return dashboard_schema.dump(Board.query.all())