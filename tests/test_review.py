import unittest

from sqlalchemy.sql import func

from app import create_app, db
from app.models import Review
from app.services import ReviewService

from tests import make_fake_book, make_fake_user


class TestReview(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app('testing')
        self.app.app_context().push()
        db.drop_all()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_add_review(self) -> None:

        # make dummy data
        user1 = make_fake_user()
        user2 = make_fake_user()
        user3 = make_fake_user()

        book1 = make_fake_book()
        book2 = make_fake_book()

        db.session.add_all([user1, user2, user3, book1, book2])
        db.session.commit()

        # book 1
        ReviewService.add_review(user1.id, book1.id, "재미있어요", 10)
        ReviewService.add_review(user2.id, book1.id, "별로네요", 5)

        # book 2
        ReviewService.add_review(user3.id, book2.id, "괜찮아요.", 9)

        count_query = db.session.query(func.count(Review.id))

        # get book1 review count
        EXPECTED = 2
        ANSWER = count_query.filter(Review.book_id == book1.id).scalar()
        self.assertEqual(EXPECTED, ANSWER)

        # get book2 review count
        EXPECTED = 1
        ANSWER = count_query.filter(Review.book_id == book2.id).scalar()
        self.assertEqual(EXPECTED, ANSWER)

    def test_check_written_review(self) -> None:
        # make dummy data
        user1 = make_fake_user()
        book1 = make_fake_book()

        db.session.add_all([user1, book1])
        db.session.commit()

        # check None
        EXPECTED = None
        ANSWER = ReviewService.get_written_review(user1.id, book1.id)

        self.assertEqual(EXPECTED, ANSWER)

        # 리뷰 작성한것 체크

        review = ReviewService.add_review(user1.id, book1.id, "좋아요.", 10)

        EXPECTED = review
        ANSWER = ReviewService.get_written_review(user1.id, book1.id)

        self.assertEqual(EXPECTED, ANSWER)

    def test_get_reviews_by_bookid(self) -> None:

        # make dummy data
        user1 = make_fake_user()
        user2 = make_fake_user()
        user3 = make_fake_user()

        book1 = make_fake_book()
        book2 = make_fake_book()

        db.session.add_all([user1, user2, user3, book1, book2])
        db.session.commit()

        # book 1
        review1 = ReviewService.add_review(user1.id, book1.id, "재미있어요", 10)
        review2 = ReviewService.add_review(user2.id, book1.id, "별로네요", 5)

        # book 2
        review3 = ReviewService.add_review(user3.id, book2.id, "괜찮아요.", 9)

        def check_sublist(small, big): return all(
            [item in big for item in small])

        EXPECTED = True
        ANSWER = check_sublist([review1, review2], ReviewService.get_reviews_by_bookid(
            book1.id))

        self.assertEqual(EXPECTED, ANSWER)

        EXPECTED = True
        ANSWER = check_sublist([review3], ReviewService.get_reviews_by_bookid(
            book2.id))
        self.assertEqual(EXPECTED, ANSWER)

        EXPECTED = False
        ANSWER = check_sublist([review2, review3], ReviewService.get_reviews_by_bookid(
            book1.id))

        self.assertEqual(EXPECTED, ANSWER)


if __name__ == '__main__':
    unittest.main()
