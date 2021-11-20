from flask.helpers import url_for

from . import mybook

from flask import render_template, request, current_app, abort, redirect, flash
from flask_login import current_user, login_required

from app.services import BookService, RentalService, UserService
from app.utility import get_stars_count, format_datetime


@mybook.route("/")
@login_required
def rented_books():
    page = request.args.get("page", default=1, type=int)
    book_per_page = current_app.config["BOOK_PER_PAGE"]

    pagination = RentalService.get_rental_and_books_paginate(current_user.id, page, book_per_page)
    books = pagination.items
    
    return render_template("mybook/rented_book_list.html",
                           items=books,
                           pagination=pagination,
                           enumerate=enumerate) 

@mybook.route("/history")
@login_required
def rented_books_history():
    page = request.args.get("page", default=1, type=int)
    book_per_page = current_app.config["BOOK_PER_PAGE"]

    pagination = RentalService.get_rental_and_books_paginate(current_user.id, page, book_per_page, True)
    books = pagination.items
    
    return render_template("mybook/rented_book_history.html",
                           items=books,
                           pagination=pagination,
                           enumerate=enumerate)
