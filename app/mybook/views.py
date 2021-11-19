from flask.helpers import url_for

from . import mybook

from flask import render_template, request, current_app, abort, redirect, flash
from flask_login import current_user

from app.services import BookService, RentalService, UserService
from app.utility import get_stars_count, format_datetime


@mybook.route("/")
def rented_books():
    page = request.args.get("page", default=1, type=int)
    book_per_page = current_app.config["BOOK_PER_PAGE"]

    rented_books = RentalService.get_rented_books(current_user.id)

    return render_template("mybook/rented_book_list.html",
                           book_list=rented_books,
                           get_stars_count=get_stars_count,
                           get_score=BookService.get_score)


@mybook.route("/history")
def rented_books_history():
    return "test"
