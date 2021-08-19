from http import HTTPStatus

from flask import request, jsonify
from flask_login import login_required, current_user
from flask_restx import Resource, Namespace, fields, abort
from marshmallow import ValidationError

from app.core.models.article import Article, article_schema, articles_schema, article_schema_for_response
from app.core.utils.resource import DefaultResource  as ListResource

api = Namespace('articles', description='게시글 관련 API')
article_model = api.model('article', {
    'title': fields.String(description='제목'),
    'content': fields.String(description='내용'),
    'board_id': fields.Integer(description='게시판 아이디'),
})


@api.route('/')
class ArticleList(ListResource):
    @login_required
    def get(self):
        """전체 게시글 list"""
        page = request.args.get('page', 1, type=int)
        articles = self.paginate(Article.query.all(), page)
        return {'data': articles_schema.dump(articles)}

    @login_required
    @api.response(201, 'Created')
    @api.expect(article_model)
    def post(self):
        """게시판 보드에 게시글 생성. 게시판 보드 ID 필요"""
        try:
            payload = article_schema.load(request.get_json())
        except ValidationError as e:
            abort(HTTPStatus.BAD_REQUEST, f'Validation Error: {e.messages}')

        payload['user_id'] = current_user.id
        article = Article(**payload)
        article.save()
        return {'data': article_schema_for_response.dump(article)}, HTTPStatus.CREATED


@api.route('/<int:article_id>/')
class ArticleRetrieve(Resource):
    @login_required
    def get(self, article_id):
        """특정 게시글"""
        article = Article.query.filter_by(id=article_id).first()
        return {'data': article_schema_for_response.dump(article)}

    @login_required
    @api.expect(article_model)
    def patch(self, article_id):
        """게시글 변경"""
        article = Article.query.get(article_id)
        payload = article_schema.load(request.get_json())

        for key, value in payload.items():
            setattr(article, key, value)
        article.update()

        return {'data': article_schema_for_response.dump(article)}

    @login_required
    @api.response(204, 'No Content')
    def delete(self, article_id):
        article = Article.query.get(article_id)
        article.delete()

        return {'data': None}
