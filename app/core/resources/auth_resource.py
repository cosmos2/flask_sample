from http import HTTPStatus

from flask import request, jsonify
from flask_login import login_required, logout_user
from flask_login import login_user
from flask_restx import Resource, Namespace, abort
from sqlalchemy.exc import NoResultFound

from app.core.models.user import signup_schema, signin_schema, user_schema, User

api = Namespace('auth', description='회원가입, 로그인, 로그아웃')


@api.route('/signup/')
class SignUp(Resource):

    def post(self):
        """회원가입"""
        payload = signup_schema.load(request.get_json())

        # 이메일 중복 확인
        if User.query.filter_by(email=payload.get('email')):
            abort(HTTPStatus.BAD_REQUEST, 'email already registered')

        password = payload.pop('password')
        password_confirm = payload.pop('password_confirm')

        if password == password_confirm:
            user = User(**payload)
            user.set_password(password)
            user.save()
        else:
            abort(HTTPStatus.BAD_REQUEST, 'No match password')


@api.route('/signin/')
class SignIn(Resource):

    def post(self):
        """로그인"""
        payload = signin_schema.load(request.get_json())
        password = payload.pop('password')

        try:
            user = User.query.filter_by(email=payload.get('email')).one()
        except NoResultFound:
            abort(HTTPStatus.UNAUTHORIZED, 'Can not find user for email')

        if not user.check_password(password):
            abort(HTTPStatus.BAD_REQUEST, 'Wrong password')
        else:
            login_user(user)
            return jsonify(user_schema.dump(user))


@api.route('/signout/')
class SignOut(Resource):

    @login_required
    def post(self):
        logout_user()
