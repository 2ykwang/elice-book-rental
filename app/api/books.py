from app.services import BookService
from flask import current_app, request
from flask_restx import Namespace, Resource

from .errors import ERROR_NOT_FOUND_RESOURCE
from .response import Response

book_api = Namespace("books")


# book list
@book_api.route("/", defaults={"page": 1})
@book_api.route("/<int:page>")
class Books(Resource):
    def get(self, page):
        # sort
        book_per_page = request.args.get(
            "per_page", default=current_app.config["BOOK_PER_PAGE"], type=int
        )

        pagination = BookService.get_books(page, book_per_page)
        book_items = list(map(lambda x: x.to_dict(), pagination.items))
        return {
            "count": len(book_items),
            "current_page": pagination.page,
            "last_page": pagination.pages,
            "has_next": pagination.has_next,
            "has_prev": pagination.has_prev,
            "books": book_items,
        }


# book detail
@book_api.route("/details/<int:book_id>")
class BookDetail(Resource):
    def get(self, book_id):

        book = BookService.get_book_by_id(book_id)
        if not book:
            return Response.make_error(ERROR_NOT_FOUND_RESOURCE, status=404)
        return book.to_dict()
