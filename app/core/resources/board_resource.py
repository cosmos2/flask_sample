from flask import request, jsonify
from flask_restx import Resource
from flask_restx import Namespace, fields

from app.core.models.board import Board, board_schema, boards_schema

api = Namespace('boards', description='board related operations')
board_model = api.model('board', {
    'title': fields.String(description='board title')
})


@api.route('/')
class BoardList(Resource):
    def get(self):
        """get board list"""
        boards = Board.query.all()
        return jsonify({'data': boards_schema.dump(boards)})

    @api.response(201, 'Created')
    @api.expect(board_model)
    def post(self):
        """create new board"""
        payload = board_schema.load(request.get_json())
        board = Board(**payload)
        board.save()
        return jsonify({'data': board_schema.dump(board)})


@api.route('/<int:board_id>/')
class BoardRetrieve(Resource):
    def get(self, board_id):
        """get a board"""
        board = Board.query.filter_by(id=board_id).first()
        return jsonify({'data': board_schema.dump(board)})

    @api.expect(board_model)
    def patch(self, board_id):
        """update board"""
        board = Board.query.get(board_id)
        payload = board_schema.load(request.get_json())

        for key, value in payload.items():
            setattr(board, key, value)
        board.update()

        return jsonify({'data': board_schema.dump(board)})

    @api.response(204, 'No Content')
    def delete(self, board_id):
        board = Board.query.get(board_id)
        board.delete()

        return jsonify({'data': None})


@api.route('<int:board_id>/articles/')
class BoardWithArticle(Resource):
    def get(self, board_id):
        """get board with articles"""
        if board := Board.query.get(board_id):
            # TODO: some articles
            pass

