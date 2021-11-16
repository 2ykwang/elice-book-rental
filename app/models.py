from datetime import datetime
from enum import unique
from . import db


class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(64), nullable=False)
    author = db.Column(db.String(64), nullable=False)
    publication_date = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(128), nullable=False)
    image_url = db.Column(db.String(150), nullable=False)


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created = db.Column(db.DateTime(), default=datetime.utcnow)
    last_login = db.Column(db.DateTime(), default=datetime.utcnow)