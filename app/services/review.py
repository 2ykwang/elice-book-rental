from typing import List, Union

from app import db
from app.models import Review
from sqlalchemy import asc, desc


class ReviewService(object):
    @staticmethod
    def add_review(
        user_id: int, book_id: int, name: str, content: str, score: int
    ) -> Review:

        review = Review(user_id, book_id, name, content, score)

        db.session.add(review)
        db.session.commit()

        return review

    @staticmethod
    def delete_review(review_id: int) -> bool:

        review = db.session.query(Review).filter(Review.id == review_id).first()

        if review:
            db.session.delete(review)
            db.session.commit()
            return True

        return False

    @staticmethod
    def is_own_review(user_id: int, review_id: int) -> bool:

        review = (
            db.session.query(Review.id)
            .filter((Review.user_id == user_id) & (Review.id == review_id))
            .first()
        )
        return review is not None

    @staticmethod
    def get_written_review(user_id: int, book_id: int) -> Union[Review, None]:

        review = (
            db.session.query(Review)
            .filter((Review.user_id == user_id) & (Review.book_id == book_id))
            .first()
        )
        return review

    @staticmethod
    def get_written_review_all(user_id: int, book_id: int) -> List[Review]:

        review = (
            db.session.query(Review)
            .filter((Review.user_id == user_id) & (Review.book_id == book_id))
            .all()
        )

        return review

    @staticmethod
    def get_reviews_by_bookid(book_id: int) -> List[Review]:

        reviews = (
            db.session.query(Review)
            .filter(Review.book_id == book_id)
            .order_by(desc(Review.created))
            .all()
        )

        return reviews
