from app.core import ma
from app.core.config import Config
from .article import ArticleSchema
from .board import BoardSchema


class DashboardSchema(BoardSchema):
    article_set = ma.Method("get_article_set")

    def get_article_set(self, obj):
        article_set = obj.article_set
        article_set.reverse()
        return ArticleSchema(many=True).dump(article_set[0:Config.PER_PAGE])


dashboard_schema = DashboardSchema(many=True)
