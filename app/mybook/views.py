from flask_sqlalchemy import Pagination

from . import mybook

from flask import render_template, request, current_app
from flask_login import current_user, login_required

from app.services import RentalService


@mybook.route("/")
@login_required
def rented_books():
    pagination = _paginate_rented_books()

    return render_template(
        "mybook/rented_book_list.html",
        items=pagination.items,
        pagination=pagination,
        enumerate=enumerate,
    )


@mybook.route("/history")
@login_required
def rented_books_history():
    pagination = _paginate_rented_books(True)

    return render_template(
        "mybook/rented_book_history.html",
        items=pagination.items,
        pagination=pagination,
        enumerate=enumerate,
    )


def _paginate_rented_books(include_returned: bool = False) -> Pagination:
    page = request.args.get("page", default=1, type=int)
    book_per_page = current_app.config["BOOK_PER_PAGE"]

    pagination = RentalService.get_rental_and_books_paginate(
        current_user.id, page, book_per_page, include_returned
    )
    return pagination
