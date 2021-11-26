from app.services import BookService, ReviewService
from flask import current_app, request
from flask_restx import Namespace, Resource

from .errors import ERROR_NOT_FOUND_RESOURCE
from .response import Response

book_api = Namespace("books", description="책에 대한 데이터를 얻기 위한 API")

parser = book_api.parser()
parser.add_argument(
    "per_page",
    type=int,
    help="페이지당 반환할 책 데이터 갯수를 설정합니다.",
    location="args",
)
parser.add_argument(
    "sort",
    type=str,
    choices=["popularity", "review", "visit"],
    help="정렬 기준을 설정합니다. popularity(인기순) review(리뷰많은순) visit(많이찾은순)",
    location="args",
)


# book list
@book_api.route("/<int:page>")
@book_api.doc(
    description="책 리스트를 반환합니다.",
    params={"page": "탐색할 페이지"},
    responses={200: "데이터 반환에 성공한 경우"},
)
class Books(Resource):
    @book_api.expect(parser)
    def get(self, page=1):
        # sort
        book_per_page = request.args.get(
            "per_page", default=current_app.config["BOOK_PER_PAGE"], type=int
        )
        sort = request.args.get("sort", default="popularity", type=str)

        pagination = BookService.get_books(page, book_per_page, sort)
        book_items = list(map(lambda x: x.to_dict(), pagination.items))
        return Response.make_response(
            {
                "count": len(book_items),
                "current_page": pagination.page,
                "last_page": pagination.pages,
                "has_next": pagination.has_next,
                "has_prev": pagination.has_prev,
                "books": book_items,
            }
        )


parser = book_api.parser()
parser.add_argument(
    "include_reviews",
    type=int,
    choices=[0, 1],
    default=1,
    help="리뷰 표시 여부를 설정합니다. ( 0 or 1 )",
    location="args",
)


# book detail
@book_api.route("/details/<int:book_id>")
@book_api.doc(
    description="책 상세 정보를 반환합니다.",
    params={"book_id": "책에대한 상세정보를 얻을 book_id"},
    responses={200: "데이터 반환에 성공한 경우", 204: "책을 찾을 수 없는 경우"},
)
class BookDetail(Resource):
    @book_api.expect(parser)
    def get(self, book_id):
        book = BookService.get_book_by_id(book_id)
        if not book:
            return Response.make_error(ERROR_NOT_FOUND_RESOURCE)

        include_reviews = request.args.get("include_reviews", default=1, type=int)

        reviews = ReviewService.get_reviews_by_bookid(book.id)

        response = {
            "book": book.to_dict(),
        }
        if include_reviews == 1:
            response["reviews"] = list(map(lambda x: x.to_dict(), reviews))

        return Response.make_response(response)
