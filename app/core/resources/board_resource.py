from flask import request
from flask_restx import Resource
from flask_restx import Namespace, fields

from app.core.models.board import Board, board_schema, boards_schema

api = Namespace('boards', description='board related operations')
_user = api.model('board', {
    'id': fields.Integer(),
    'title': fields.String(description='board title')
})


@api.route('/')
class BoardList(Resource):
    @api.doc('Board list', response={200: 'OK'})
    def get(self):
        boards = Board.query.all()
        return {'data': boards_schema.dump(boards)}

    def post(self):
        payload = board_schema.load(request.get_json())
        title = payload.get('title')
        board = Board(title=title)
        board.save()
        return {'data': board_schema.dump(board)}


@api.route('/<int:board_id>/')
class BoardRetrieve(Resource):
    @api.doc('Board retrieve', response={200: 'OK'})
    def get(self, board_id):
        board = Board.query.filter_by(id=board_id).first()
        return {'data': board_schema.dump(board)}

