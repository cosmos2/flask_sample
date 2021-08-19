from .board import BoardSchema
from .article import ArticleSchemaForResponse
from app.core import ma


class DashboardSchema(BoardSchema):
    article_set = ma.List(ma.Nested(ArticleSchemaForResponse))


dashboard_schema = DashboardSchema(many=True)
