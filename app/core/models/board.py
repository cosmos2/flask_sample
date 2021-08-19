from app.core import db, ma
from app.core.utils.models import BaseModel
from app.core.utils.schema import CamelCaseSchema

__all__ = (
    'Board',
    'board_schema',
    'boards_schema'
)


class Board(BaseModel, db.Model):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class BoardSchema(CamelCaseSchema, ma.SQLAlchemySchema):
    class Meta:
        model = Board

    id = ma.auto_field()
    name = ma.auto_field()


board_schema = BoardSchema()
boards_schema = BoardSchema(many=True)
