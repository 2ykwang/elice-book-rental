from typing import Any, Union, List, Tuple
from datetime import datetime, timedelta
from sqlalchemy import desc
from app.models import Book, Rental
from app.utility import korea_datetime

from app import db


class RentalService(object):

    # @staticmethod
    # def get_rental_records_by_userid(user_id: int, include_returned: bool = False) -> Union[List[Rental], None]:
    #     if include_returned:
    #         records = db.session.query(Rental).filter(
    #             Rental.user_id == user_id).all()
    #     else:
    #         records = db.session.query(Rental).filter(
    #             (Rental.user_id == user_id) & (Rental.returned == False)).all()

    #     return records if len(records) > 0 else None

    @staticmethod
    def get_rental_and_books(user_id: int, include_returned: bool = False) -> Union[List[Tuple[Book, Rental]], None]:
        joined_query = books = db.session.query(Book, Rental).join(Rental, Rental.book_id == Book.id)
        
        if include_returned:
            books = joined_query.filter((Rental.user_id == user_id)).order_by(desc(Rental.created)).all() 
        else:
            books = joined_query.filter((Rental.user_id == user_id) & (Rental.returned == False)).order_by(desc(Rental.created)).all()

        return books if len(books) > 0 else None

    @staticmethod
    def add_rental(user_id: int, book_id: int, period: int = 7) -> Rental:
        rental = Rental()
        rental.user_id = user_id
        rental.book_id = book_id
        rental.returned = False
        rental.duration = korea_datetime() + timedelta(days=period)

        db.session.add(rental)
        db.session.commit()
        return rental

    @staticmethod
    def return_book(user_id: int, book_id: int) -> bool:
        rental = db.session.query(Rental).filter(
            (Rental.user_id == user_id) & (Rental.book_id == book_id) & (Rental.returned == False)).first()
        if rental is not None:
            rental.returned = True
            db.session.add(rental)
            db.session.commit()
            return True

        return False

    @staticmethod
    def is_user_rented_book(user_id: int, book_id: int, include_returned: bool = False) -> bool:
        if include_returned:
            rental = db.session.query(Rental.id).filter(
                (Rental.user_id == user_id) & (Rental.book_id == book_id)).first()
        else:
            rental = db.session.query(Rental.id).filter(
                (Rental.user_id == user_id) & (Rental.book_id == book_id) & (Rental.returned == False)).first()

        return rental is not None
