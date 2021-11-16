from datetime import datetime
from . import db


class Book(db.Model):
    __tablename__ = "books"
    
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    publication_date = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    isbn = db.Column(db.BigInteger, nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(128), nullable=False)
    image_url = db.Column(db.String(150), nullable=False)
