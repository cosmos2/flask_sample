from app.core import db, ma
from app.core.utils.models import BaseModel
from app.core.utils.schema import CamelCaseSchema

__all__ = (
    'Article',
    'article_schema',
    'articles_schema',
    'article_schema_for_response',
)


class Article(BaseModel, db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text, nullable=True)
    board_id = db.Column(db.Integer, db.ForeignKey('boards.id', ondelete='CASCADE'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)

    # relations
    user = db.relationship('User', backref='article_set', lazy=True)
    board = db.relationship('Board', backref='article_set', lazy=True)


class ArticleSchema(CamelCaseSchema, ma.SQLAlchemySchema):
    class Meta:
        model = Article
        include_fk = True

    id = ma.auto_field()
    title = ma.auto_field()
    content = ma.auto_field()
    board_id = ma.auto_field()


class ArticleSchemaForResponse(ArticleSchema):
    user_name = ma.Method('get_user_name')

    def get_user_name(self, obj):
        return obj.user.fullname if obj.user else None


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
article_schema_for_response = ArticleSchemaForResponse()