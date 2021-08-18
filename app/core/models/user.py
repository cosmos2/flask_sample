from flask_login import UserMixin

from app.core import db, ma, bcrypt
from app.core.utils.models import BaseModel

__all__ = (
    'User',
    'user_schema',
    'users_schema',
    'signin_schema',
    'signup_schema',
)


class User(UserMixin, BaseModel, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    is_staff = db.Column(db.Boolean, default=False)

    def set_password(self, password: str):
        if password:
            self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password: str):
        return password and bcrypt.check_password_hash(self.password, password)


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    fullname = ma.auto_field()
    email = ma.auto_field()
    is_staff = ma.auto_field()


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class SignInSchema(ma.Schema):
    email = ma.Email(
        required=True,
        metadata={
            'description': '이메일 주소',
            'example': 'harrp@gryffindor.co.uk',
        },
    )
    password = ma.String(
        required=True,
        metadata={
            'description': '패스워드',
            'example': 'dlkfji293!23j',
        },
    )


class SignUpSchema(SignInSchema):
    fullname = ma.String(
        required=True,
        metadata={
            'description': '사용자 이름',
            'example': 'Harry Potter',
        },
    )
    password_confirm = ma.String(
        required=True,
        metadata={
            'description': '패스워드 재입력',
            'example': 'dlkfji293!23j',
        },
    )


signin_schema = SignInSchema()
signup_schema = SignUpSchema()