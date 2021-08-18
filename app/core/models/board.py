from app.core import db, ma
from app.core.utils.models import BaseModel

__all__ = (
    'Board',
    'board_schema',
    'boards_schema'
)


class Board(BaseModel, db.Model):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))


class BoardSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Board

    id = ma.auto_field()
    title = ma.auto_field()


board_schema = BoardSchema()
boards_schema = BoardSchema(many=True)
