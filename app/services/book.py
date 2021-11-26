from typing import Dict, Union

from app import db
from app.models import Book, Review
from flask_sqlalchemy import Pagination
from sqlalchemy.sql import desc, func
from sqlalchemy.sql.expression import asc

BOOK_SORT_POPULARITY = "popularity"
BOOK_SORT_REVIEW = "review"
BOOK_SORT_VISIT = "visit"
DEFAULT_SORT = BOOK_SORT_POPULARITY

sort_available = [BOOK_SORT_POPULARITY, BOOK_SORT_REVIEW, BOOK_SORT_VISIT]


class BookService(object):
    @staticmethod
    def get_books(
        current_page: int, book_per_page: int, sort: str = BOOK_SORT_POPULARITY
    ) -> Pagination:

        query = BookService._book_sort(sort)

        pagination = query.paginate(current_page, book_per_page, error_out=False)
        return pagination

    @staticmethod
    def search_query(
        keyword: str,
        current_page: int,
        book_per_page: int,
        sort: str = BOOK_SORT_POPULARITY,
    ):
        query = BookService._book_sort(sort).filter(
            Book.book_name.like(f"%{keyword}%") | Book.description.like(f"%{keyword}%")
        )

        pagination = query.paginate(current_page, book_per_page, error_out=False)
        return pagination

    # NOTE: 중복되는 코드 메소드 추출
    @staticmethod
    def _book_sort(sort):
        if sort not in sort_available:
            sort = DEFAULT_SORT

        if sort == BOOK_SORT_POPULARITY:
            query = (
                db.session.query(Book)
                .outerjoin(Review, Review.book_id == Book.id)
                .group_by(Book.book_name, Book.id)
                .order_by(desc(func.avg(Review.score)), desc(func.count(Book.review)))
            )
        elif sort == BOOK_SORT_REVIEW:
            query = (
                db.session.query(Book)
                .outerjoin(Review, Review.book_id == Book.id)
                .group_by(Book.book_name, Book.id)
                .order_by(desc(func.count(Book.review)))
            )
        elif sort == BOOK_SORT_VISIT:
            query = db.session.query(Book).order_by(desc(Book.viewer))

        return query

    @staticmethod
    def get_book_by_id(book_id: int) -> Union[Book, None]:
        book = db.session.query(Book).filter(Book.id == book_id).first()
        return book

    @staticmethod
    def increase_viewer(book_id: int, count: int = 1) -> None:
        book = db.session.query(Book).filter(Book.id == book_id).first()
        book.viewer += count
        db.session.add(book)
        db.session.commit()

    @staticmethod
    def increase_stock(book_id: int, count: int = 1) -> None:
        book = db.session.query(Book).filter(Book.id == book_id).first()
        book.stock += count
        db.session.add(book)
        db.session.commit()

    @staticmethod
    def decrease_stock(book_id: int, count: int = 1) -> None:
        book = db.session.query(Book).filter(Book.id == book_id).first()
        book.stock -= count
        db.session.add(book)
        db.session.commit()

    @staticmethod
    def get_score(book_id: int) -> Union[Dict, None]:

        # 자신을 참조하고 있는 review row 뽑아오기
        # reviews = db.session.query(Review.score).filter(
        #     Review.book_id == book_id).all()
        # book = db.session.query(Book).filter(Book.id == book_id).first()
        # book.review.query(func.sum())
        # count = len(book.review)
        # if count > 0:
        #     result = {'score': 0, 'count': 0}
        #     result['score'] = sum([review.score for review in book.review])/count
        #     result['count'] = count
        #     return result

        # NOTE: with-entities 라는 아주 좋은 함수가 있었다.

        query_result = dict(
            Book.query.with_entities(
                func.avg(Review.score).label("score"), func.count().label("count")
            )
            .filter(Review.book_id == book_id)
            .first()
        )

        return query_result if query_result["count"] > 0 else None
