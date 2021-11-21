from typing import Any, Union, List, Tuple
from sqlalchemy import desc
from app.models import Book, Rental, Review, User
from app.utility import korea_datetime, dict_combine

from app import db


class ReviewService(object):

    @staticmethod
    def add_review(user_id: int, book_id: int, content: str, score: int) -> Review:

        review = Review(user_id, book_id, content, score)

        db.session.add(review)
        db.session.commit() 
        
        return review

    @staticmethod
    def get_written_review(user_id: int, book_id: int) -> Union[Review, None]:

        review = db.session.query(Review).filter(
            (Review.user_id == user_id) & (Review.book_id == book_id)).first()
        
        return review

    @staticmethod
    def get_written_review_all(user_id: int, book_id: int) -> List[Review]:

        review = db.session.query(Review).filter(
            (Review.user_id == user_id) & (Review.book_id == book_id)).all()
        
        return review

    @staticmethod
    def get_reviews_by_bookid(book_id: int) -> List[Review]:

        reviews = db.session.query(Review).filter(
            Review.book_id == book_id
        ).all()

        return reviews
