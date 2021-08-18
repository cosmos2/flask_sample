from flask import request, jsonify, session
from flask_restx import Resource
from flask_restx import Namespace, fields
from sqlalchemy.exc import NoResultFound

from app.core.models.user import signup_schema, signin_schema, User

api = Namespace('auth', description='sign up, sign in, sign out')


@api.route('/signup/')
class SignUp(Resource):

    def post(self):
        """회원가입"""
        payload = signup_schema.load(request.get_json())
        password = payload.pop('password')
        password_confirm = payload.pop('password_confirm')

        if password == password_confirm:
            user = User(**payload)
            user.set_password(password)
            user.save()
        else:
            # ValueError
            pass


@api.route('/signin/')
class SignIn(Resource):

    def post(self):
        """로그인"""
        payload = signin_schema.load(request.get_json())
        password = payload.pop('password')

        try:
            user = User.query.filter_by(email=payload.get('email')).one()
        except NoResultFound:
            # TODO: no user error
            return 'no user'

        if not user.check_password(password):
            # TODO: password not match error
            return 'not match password'
        else:
            # TODO: login process
            session['user_id'] = user.id
            return 'ok login'
