from app.core import db, ma
from app.core.utils.models import BaseModel

__all__ = (
    'Article',
    'article_schema',
    'articles_schema',
)


class Article(BaseModel, db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=True)
    board_id = db.Column(db.Integer, db.ForeignKey('boards.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # relations
    user = db.relationship('User', backref='article_set', lazy=True)
    board = db.relationship('Board', backref='article_set', lazy=True)


class ArticleSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Article
        include_fk = True

    id = ma.auto_field()
    content = ma.auto_field()
    board_id = ma.auto_field()
    user_id = ma.auto_field()


article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)
