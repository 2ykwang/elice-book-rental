# sleep function
import random
import time
import unittest
from http import HTTPStatus

from app import create_app, db
from app.models import Book, User

from tests import make_fake_book, make_fake_user, make_review, make_user


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app("testing")
        self.app.app_context().push()
        # db in
        db.drop_all()
        db.create_all()

        # dummy 데이터 만들기
        self.users = [make_fake_user() for _ in range(10)]

        self.books = [make_fake_book() for _ in range(3)]

        db.session.add_all(self.users)
        db.session.add_all(self.books)
        db.session.commit()

        # http client
        self.client = self.app.test_client()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_book_details(self) -> None:

        all_books = list(map(lambda x: x.to_dict(), self.books))

        response = self.client.get("/api/books/details/1?include_reviews=0")
        response_json = response.json

        self.assertIn(response_json["result"]["book"], all_books)

        reviews = [
            make_review(
                user.id,
                self.books[0].id,
                user.name,
                f"리뷰{random.randint(0,9999)}",
                random.randint(3, 10),
            )
            for user in self.users
        ]
        db.session.add_all(reviews)
        db.session.commit()

        all_reviews = list(map(lambda x: x.to_dict(), reviews))
        response = self.client.get("/api/books/details/1?include_reviews=1")
        response_json = response.json

        for review in all_reviews:
            self.assertIn(review, response_json["result"]["reviews"])

    def test_list_books(self) -> None:

        response = self.client.get("/api/books/1?per_page=2")
        response_json = response.json

        # check status code
        response_status_code = response.status_code
        status_code = response_json["status"]
        self.assertEqual(HTTPStatus.OK, response_status_code)
        self.assertEqual(HTTPStatus.OK, status_code)

        # check pagination

        self.assertEqual(2, response_json["result"]["count"])
        self.assertEqual(1, response_json["result"]["current_page"])
        self.assertEqual(2, response_json["result"]["last_page"])
        self.assertEqual(True, response_json["result"]["has_next"])
        self.assertEqual(False, response_json["result"]["has_prev"])

        # check response data

        response = self.client.get("/api/books/1?per_page=3")
        response_json = response.json

        book_items = response_json["result"]["books"]

        for book in self.books:
            self.assertIn(book.to_dict(), book_items)


if __name__ == "__main__":
    unittest.main()
