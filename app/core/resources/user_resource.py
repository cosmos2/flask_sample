from flask_restx import Namespace
from flask_restx import Resource

from app.core.models.user import User, user_schema, users_schema
from app.core.utils.decorator import admin_only

api = Namespace('users', description='유저정보 관련 API for staff')


@api.route('/')
class UserList(Resource):

    @admin_only
    @api.doc('User list', response={200: 'OK'})
    def get(self):
        """모든 유저 list"""
        users = User.query.all()
        return {'data': users_schema.dump(users)}


@api.route('/<int:user_id>/')
class UserRetrieve(Resource):

    @admin_only
    @api.doc('User retrieve', response={200: 'OK'})
    def get(self, user_id):
        """특정 유저 정보"""
        user = User.query.filter_by(id=user_id).first()
        return {'data': user_schema.dump(user)}

    @admin_only
    @api.response(204, 'No Content')
    def delet(self, user_id):
        """유저 삭제"""
        user = User.query.get(user_id)
        user.delet()

        return {'data': None} , 204
