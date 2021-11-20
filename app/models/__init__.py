from typing import Dict, Union, Tuple
from enum import unique

from flask_sqlalchemy import BaseQuery

from app import db, login_manager
from app.utility import korea_datetime
from datetime import timedelta

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app.utility import format_datetime  
class Rental(db.Model):
    """사용자 책 대여 Model"""
    __tablename__ = 'rental'

    id = db.Column(db.Integer, primary_key=True)
    returned = db.Column(db.Boolean, nullable=False)
    created = db.Column(db.DateTime, default=korea_datetime)
    return_date = db.Column(db.DateTime)
    duration = db.Column(db.DateTime)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def to_dict(self):
        result = {
            "returned": self.returned,
            "created": self.created,
            "return_date": self.return_date,
            "duration": self.duration,
            "book_id": self.book_id,
            "user_id": self.user_id,
        }
        return result

class Review(db.Model):
    """책 후기 Model"""
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=korea_datetime)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, content: str = "", score: int = 0, book_id: int = None, user_id: int = None):
        """리뷰 Model 객체 초기화

        Args:
            content (str, optional): 리뷰 내용. Defaults to "".
            score (int, optional): 점수. Defaults to 0.
            book_id (int, optional): user_id fk. Defaults to None.
            user_id (int, optional): book_id fk. Defaults to None.
        """
        self.content = content
        self.score = score
        self.book_id = book_id
        self.user_id = user_id

    def to_dict(self):
        result = { 
            "content": self.content,
            "score": self.score,
            "created": self.created,
            "book_id": self.book_id,
            "user_id": self.user_id,
        }
        return result

class Book(db.Model):
    """책 Model"""
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(64), nullable=False)
    author = db.Column(db.String(64), nullable=False)
    publication_date = db.Column(db.DateTime, nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.Text, nullable=False)
    viewer = db.Column(db.Integer, default=0)  # 조회수
    link = db.Column(db.String(128), nullable=False)
    image_url = db.Column(db.String(150), nullable=False)
    stock = db.Column(db.Integer, default=10)

    rental = db.relationship(Rental, backref='book')
    review = db.relationship(Review, backref='book')

    def to_dict(self):
        result = {
            "book_name": self.book_name,
            "publisher": self.publisher,
            "author": self.author,
            "publication_date": self.publication_date,
            "pages": self.pages,
            "isbn": self.isbn,
            "description": self.description,
            "viewer": self.viewer,
            "link": self.link,
            "image_url": self.image_url,
            "stock": self.stock,
            "rental_count": len(self.rental),
            "review_count": len(self.review),
        }
        return result


class User(UserMixin, db.Model):
    """사용자 Model"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created = db.Column(db.DateTime, default=korea_datetime)
    last_login = db.Column(db.DateTime, default=korea_datetime)

    rental = db.relationship(Rental, backref='user')
    review = db.relationship(Review, backref='user')

    def __init__(self, name: str = "", email: str = "", password_hash: str = "") -> None:
        """사용자 Model 객체 초기화

        Args:
            name (str): 이름
            email (str): 아이디(이메일)
            password_hash (str): 암호화된 패스워드
        """
        self.name = name
        self.email = email
        self.password_hash = password_hash

    def to_dict(self):
        a = self
        
        result = { 
            "name": self.name,
            "email": self.email,
            "created": self.created,
            "last_login": self.last_login,
            "rental_count": len(self.rental), 
            "review_count": len(self.review), 
        }
        return result


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
