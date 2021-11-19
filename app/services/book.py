from typing import Union, Dict
from flask_sqlalchemy import Pagination
from app.models import Book, Review
from app import db


class BookService(object):

    @staticmethod
    def get_books(current_page: int, book_per_page: int) -> Pagination:
        query = Book.query
        pagination = query.paginate(
            current_page, book_per_page, error_out=False)
        return pagination

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
        reviews = db.session.query(Review.score).filter(
            Review.book_id == book_id).all()

        count = len(reviews)
        if count > 0:
            result = {'score': 0, 'count': 0}
            result['score'] = sum([review.score for review in reviews])/count
            result['count'] = count
            return result
        return None