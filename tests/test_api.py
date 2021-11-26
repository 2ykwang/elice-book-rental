# sleep function
import random
import time
import unittest
from http import HTTPStatus
from typing import List

from app import create_app, db
from app.models import Book, User
from flask_sqlalchemy.model import Model

from tests import make_fake_book, make_fake_user, make_review, make_user


def _reset(items: List[Model]) -> None:
    for item in items:
        db.session.delete(item)
    db.session.commit()


class TestAPI(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app("testing")
        self.app.app_context().push()
        # db in
        db.drop_all()
        db.create_all()

        # http client
        self.client = self.app.test_client()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_book_search(self) -> None:
        COUNT = 10
        dummy_books = [make_fake_book() for _ in range(COUNT)]
        titles = [
            "aaaa",
            "bbbb",
            "ccc aaa ccc",
            "eeee",
            "aaaa",
            "aaaa",
            "aa",
            "b",
            "c",
            "abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg",
        ]
        for i in range(COUNT):
            dummy_books[i].book_name = titles[i]
            dummy_books[i].description = titles[i]

        db.session.add_all(dummy_books)
        db.session.commit()

        cases = [
            {"expected": 5, "query": "aa"},
            {"expected": 1, "query": "bb"},
            {"expected": 3, "query": "c"},
            {"expected": 2, "query": "e"},
            {"expected": 6, "query": "a"},
        ]
        for case in cases:
            response = self.client.get(
                f"/api/books/search?q={case['query']}&per_page={COUNT}"
            )
            response_json = response.json

            self.assertEqual(case["expected"], response_json["result"]["count"])

        _reset(dummy_books)

    def test_book_details(self) -> None:

        books = [make_fake_book() for _ in range(3)]
        db.session.add_all(books)
        db.session.commit()

        users = [make_fake_user() for _ in range(10)]
        db.session.add_all(users)
        db.session.commit()

        all_books = list(map(lambda x: x.to_dict(), books))

        response = self.client.get("/api/books/details/1?include_reviews=0")
        response_json = response.json

        self.assertIn(response_json["result"]["book"], all_books)

        reviews = [
            make_review(
                user.id,
                books[0].id,
                user.name,
                f"리뷰{random.randint(0,9999)}",
                random.randint(3, 10),
            )
            for user in users
        ]
        db.session.add_all(reviews)
        db.session.commit()

        all_reviews = list(map(lambda x: x.to_dict(), reviews))
        response = self.client.get(
            f"/api/books/details/{books[0].id}?include_reviews=1"
        )
        response_json = response.json

        for review in all_reviews:
            self.assertIn(review, response_json["result"]["reviews"])

        _reset(reviews)

        _reset(books)

        _reset(users)

    def test_list_books(self) -> None:

        books = [make_fake_book() for _ in range(3)]
        db.session.add_all(books)
        db.session.commit()

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

        for book in books:
            self.assertIn(book.to_dict(), book_items)

        _reset(books)


if __name__ == "__main__":
    unittest.main()
