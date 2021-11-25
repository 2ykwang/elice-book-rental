from datetime import timedelta
from typing import List, Tuple, Union

from app import db
from app.models import Book, Rental
from app.utility import dict_combine, korea_datetime
from flask_sqlalchemy import Pagination
from sqlalchemy import desc


class RentalService(object):
    @staticmethod
    def get_rental_and_books(
        user_id: int, include_returned: bool = False
    ) -> Union[List[Tuple[Book, Rental]], None]:
        joined_query = db.session.query(Book, Rental).join(
            Rental, Rental.book_id == Book.id
        )

        filter = (
            (Rental.user_id == user_id)
            if include_returned
            else ((Rental.user_id == user_id) & (Rental.returned.is_(False)))
        )

        books = joined_query.filter(filter).order_by(desc(Rental.created)).all()

        return books if len(books) > 0 else None

    @staticmethod
    def get_rental_and_books_paginate(
        user_id: int,
        current_page: int,
        book_per_page: int,
        include_returned: bool = False,
    ) -> Pagination:

        joined_query = db.session.query(Rental, Book).join(
            Rental, Rental.book_id == Book.id
        )

        filter = (
            (Rental.user_id == user_id)
            if include_returned
            else ((Rental.user_id == user_id) & (Rental.returned.is_(False)))
        )

        pagination = (
            joined_query.filter(filter)
            .order_by(desc(Rental.created))
            .paginate(current_page, book_per_page, error_out=False)
        )

        # TODO: 이 부분이 좀 신경쓰임 테이블 병합하고 새로운 데이터를 어떻게 처리해야하는지 알아보자.
        # pagination.items = [
        #     dict_combine(x.Book.to_dict(), x.Rental.to_dict()) for x in pagination.items
        # ]

        return pagination

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
        rental = (
            db.session.query(Rental)
            .filter(
                (
                    (Rental.user_id == user_id)
                    & (Rental.book_id == book_id)
                    & (Rental.returned.is_(False))
                )
            )
            .first()
        )
        if rental is not None:
            rental.returned = True
            rental.return_date = korea_datetime()
            db.session.add(rental)
            db.session.commit()
            return True

        return False

    @staticmethod
    def is_user_rented_book(
        user_id: int, book_id: int, include_returned: bool = False
    ) -> bool:
        filter = (
            (Rental.user_id == user_id) & (Rental.book_id == book_id)
            if include_returned
            else (
                (Rental.user_id == user_id)
                & (Rental.book_id == book_id)
                & (Rental.returned.is_(False))
            )
        )

        rental = db.session.query(Rental.id).filter(filter).first()

        return rental is not None
