from flask_restx import Resource

from app.core.config import Config


class DefaultResource(Resource):

    def paginate(self, query_list, page=1):
        per_page = Config.PER_PAGE
        start, end = 0, per_page

        if page == 1:
            return query_list[start:end]
        else:
            start = (page - 1) * per_page
            end = page * per_page
            return query_list[start:end]
