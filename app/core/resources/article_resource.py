from flask import request, jsonify
from flask_restx import Resource
from flask_restx import Namespace, fields

from app.core.models.article import Article, article_schema, articles_schema

api = Namespace('articles', description='articles related operations')
article_model = api.model('article', {
    'content': fields.String(description='내용'),
    'board_id': fields.Integer(description='게시판 아이디'),
    'user_id': fields.Integer(description='사용자 아이디'),
})


@api.route('/')
class ArticleList(Resource):
    def get(self):
        """get article list"""
        articles = Article.query.all()
        return jsonify({'data': articles_schema.dump(articles)})

    @api.response(201, 'Created')
    @api.expect(article_model)
    def post(self):
        """create new article"""
        payload = article_schema.load(request.get_json())
        board = Article(**payload)
        board.save()
        return jsonify({'data': article_schema.dump(board)})


@api.route('/<int:article_id>/')
class ArticleRetrieve(Resource):
    def get(self, article_id):
        """get a article"""
        board = Article.query.filter_by(id=article_id).first()
        return jsonify({'data': article_schema.dump(board)})

    @api.expect(article_model)
    def patch(self, article_id):
        """update article"""
        article = Article.query.get(article_id)
        payload = article_schema.load(request.get_json())

        for key, value in payload.items():
            setattr(article, key, value)
        article.update()

        return jsonify({'data': article_schema.dump(article)})

    @api.response(204, 'No Content')
    def delete(self, article_id):
        article = Article.query.get(article_id)
        article.delete()

        return jsonify({'data': None})
