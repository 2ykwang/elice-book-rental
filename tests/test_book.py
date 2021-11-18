import unittest
from app import create_app, db
from app.models import User, Rental
from fake import make_fake_book, make_fake_user, make_review


class TestBook(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app('testing')
        self.app.app_context().push()
        db.drop_all()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_rent_book(self) -> None:
        pass

    def test_get_score_expected_None_when_no_data(self) -> None:
        book = make_fake_book()
        book.stock = 10
        EXPECTED = None
        ANSWER = book.get_score()["score"]

        self.assertEqual(EXPECTED, ANSWER)

    def test_get_score(self) -> None:
        # 더미 데이터 생성
        user1 = make_fake_user()
        user2 = make_fake_user()
        user3 = make_fake_user()
        book = make_fake_book()
        book.stock = 10

        db.session.add_all([book, user1, user2, user3])
        db.session.commit()

        # 후기 생성

        reviews = [
            make_review("괜찮네요.", 10, book.id, user1.id),
            make_review("재미있었어요!", 8, book.id, user2.id),
            make_review("전 별로였어요", 6, book.id, user3.id),
        ]
        db.session.add_all(reviews)
        db.session.commit()

        # 점수 평균
        EXPECTED = (10+8+6)/3
        ANSWER = book.get_score()["score"]

        self.assertEqual(EXPECTED, ANSWER)

    def test_decrease_and_increase_book_quantity(self) -> None:

        book = make_fake_book()
        book.stock = 10

        db.session.add(book)
        db.session.commit()

        book.decrease_stock(3)

        EXPECTED = 7
        self.assertEqual(EXPECTED, book.stock)

        book.increase_stock(5)

        EXPECTED = 12
        self.assertEqual(EXPECTED, book.stock)


if __name__ == '__main__':
    unittest.main()
