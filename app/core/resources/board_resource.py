from http import HTTPStatus

from flask import request
from flask_login import login_required
from flask_restx import Resource, Namespace, fields

from app.core.models.article import articles_schema
from app.core.models.board import Board, board_schema, boards_schema
from app.core.utils.resource import DefaultResource  as ListResource

api = Namespace('boards', description='board related operations')
board_model = api.model('board', {
    'name': fields.String(description='board title')
})


@api.route('/')
class BoardList(ListResource):
    def get(self):
        """get board list"""
        page = request.args.get('page', 1, type=int)
        boards = self.paginate(Board.query.all(), page)
        return {'data': boards_schema.dump(boards)}

    @login_required
    @api.response(201, 'Created')
    @api.expect(board_model)
    def post(self):
        """새로운 게시판 생성"""
        payload = board_schema.load(request.get_json())
        board = Board(**payload)
        board.save()
        return {'data': board_schema.dump(board)}, HTTPStatus.CREATED


@api.route('/<int:board_id>/')
class BoardRetrieve(Resource):
    @login_required
    def get(self, board_id):
        """get a board"""
        board = Board.query.filter_by(id=board_id).first()
        return {'data': board_schema.dump(board)}

    @login_required
    @api.expect(board_model)
    def patch(self, board_id):
        """update board"""
        board = Board.query.get(board_id)
        payload = board_schema.load(request.get_json())

        for key, value in payload.items():
            setattr(board, key, value)
        board.update()

        return {'data': board_schema.dump(board)}

    @login_required
    @api.response(204, 'No Content')
    def delete(self, board_id):
        board = Board.query.get(board_id)
        board.delete()

        return {'data': None}


@api.route('/<int:board_id>/articles/')
class BoardWithArticle(ListResource):
    @login_required
    def get(self, board_id):
        """get board with articles"""
        result = {'data': None}
        page = request.args.get('page', 1, type=int)
        if board := Board.query.get(board_id):
            result['data'] = articles_schema.dump(self.paginate(board.article_set, page))

        return result

