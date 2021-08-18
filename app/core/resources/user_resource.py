from flask import request
from flask_restx import Resource
from flask_restx import Namespace, fields

from app.core.models.user import User, user_schema, users_schema

api = Namespace('users', description='user related operations')
_user = api.model('user', {
    'email': fields.String(required=True, description='user email address'),
    'username': fields.String(required=True, description='user username'),
    'password': fields.String(required=True, description='user password'),
    'public_id': fields.String(description='user Identifier')
})


@api.route('/')
class UserList(Resource):
    @api.doc('User list', response={200: 'OK'})
    def get(self):
        users = User.query.all()
        return {'data': users_schema.dump(users)}


@api.route('/<int:user_id>/')
class UserRetrieve(Resource):
    @api.doc('User retrieve', response={200: 'OK'})
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        return {'data': user_schema.dump(user)}