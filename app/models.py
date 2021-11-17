from datetime import datetime
from enum import unique
from . import db


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
    link = db.Column(db.String(128), nullable=False)
    image_url = db.Column(db.String(150), nullable=False)


# class Stock(db.Model):
#     """책 재고 Model"""
#     pass


class User(db.Model):
    """사용자 Model"""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, default=datetime.utcnow)


class Rental(db.Model):
    """사용자 책 대여 Model"""
    __tablename__ = 'rental'

    id = db.Column(db.Integer, primary_key=True)
    returned = db.Column(db.Boolean, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    return_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Review(db.Model):
    """책 후기 Model"""
    __tablename__ = 'review'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    score = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
