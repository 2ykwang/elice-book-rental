from app.models import User, Book, Review
from app.utility import korea_datetime
import random
import string
import datetime


def make_user(name: str, email: str, password: str) -> User:
    user = User(name, email, password)
    return user


def make_review(user_id: int, book_id: int, content: str, score: int) -> Review:
    review = Review(user_id, book_id, content, score)
    return review


def make_fake_user() -> User:
    return make_user(__random_string(6), f"{__random_string(8)}@{__random_string(5)}.com", __random_string(10))


def make_fake_book() -> Book:
    book = Book()
    book.book_name = __random_string(5)
    book.publisher = __random_string(5)
    book.author = __random_string(5)
    book.publication_date = korea_datetime()
    book.pages = random.randrange(100, 300)
    book.isbn = __random_string(5)
    book.description = __random_string(5)
    book.link = f"https://{__random_string(5)}"
    book.image_url = f'{__random_string(5)}.jpg'
    return book


def __random_string(size=10, chars=string.ascii_uppercase+string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))
