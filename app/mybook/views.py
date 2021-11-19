from flask.helpers import url_for

from . import mybook

from flask import render_template, request, current_app, abort, redirect, flash
from flask_login import current_user, login_required

from app.services import BookService, RentalService, UserService
from app.utility import get_stars_count, format_datetime


@mybook.route("/")
@login_required
def rented_books():
    rented_books = RentalService.get_rental_and_books(current_user.id)

    return render_template("mybook/rented_book_list.html",
                           items=rented_books)


@mybook.route("/history")
@login_required
def rented_books_history():
    rented_books = RentalService.get_rental_and_books(current_user.id, True)

    return render_template("mybook/rented_book_history.html", 
                           items=rented_books)
