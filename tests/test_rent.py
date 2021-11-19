import unittest

from app import create_app, db
from app.services import RentalService

from tests import make_fake_book, make_fake_user


class TestBook(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app('testing')
        self.app.app_context().push()
        db.drop_all()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_get_rental_and_books(self) -> None:
        user = make_fake_user()
        book = make_fake_book()
        book2 = make_fake_book()

        db.session.add_all([book, book2, user])
        db.session.commit()

        RentalService.add_rental(user.id, book.id, 7)
        RentalService.add_rental(user.id, book2.id, 7)
        RentalService.return_book(user.id, book.id)
        
        target = RentalService.get_rental_and_books(user.id)[0]

        EXPECTED = book2.book_name
        ANSWER = target.Book.book_name
        self.assertEqual(EXPECTED, ANSWER)

    def test_book_return_expected_true(self) -> None:
        user = make_fake_user()
        book = make_fake_book()

        db.session.add_all([book, user])
        db.session.commit()

        RentalService.add_rental(user.id, book.id, 7)

        EXPECTED = True
        ANSWER = RentalService.return_book(user.id, book.id)

        self.assertEqual(EXPECTED, ANSWER)

    def test_is_user_rented_book_expected_True(self) -> None:
        user = make_fake_user()
        book = make_fake_book()

        db.session.add_all([book, user])
        db.session.commit()

        RentalService.add_rental(user.id, book.id, 7)

        EXPECTED = True
        ANSWER = RentalService.is_user_rented_book(user.id, book.id)

        self.assertEqual(EXPECTED, ANSWER)


if __name__ == '__main__':
    unittest.main()
