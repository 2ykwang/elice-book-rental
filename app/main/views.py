from flask.helpers import url_for

from . import main

from flask import render_template, request, current_app, redirect, flash
from flask_login import current_user, login_required

from app.services import BookService, RentalService
from app.utility import get_stars_count, format_datetime
from app.decorator import is_exists_book


@main.route("/")
def index():
    page = request.args.get("page", default=1, type=int)
    book_per_page = current_app.config["BOOK_PER_PAGE"]

    pagination = BookService.get_books(page, book_per_page)
    books = pagination.items

    return render_template("book_list.html",
                           book_list=books,
                           pagination=pagination,
                           enumerate=enumerate,
                           get_stars_count=get_stars_count,
                           get_score=BookService.get_score)


@main.route("/book/<int:id>")
@is_exists_book(redirect_endpoint='main.index')
def book_detail(id):

    book = BookService.get_book_by_id(id)
    BookService.increase_viewer(book.id)

    return render_template("book_detail.html",
                           book=book,
                           get_stars_count=get_stars_count,
                           get_score=BookService.get_score)


@main.route("/book/<int:id>/rent", methods=["POST"])
@login_required
@is_exists_book()
def book_rent(id):
    book = BookService.get_book_by_id(id)
    # 재고가 없을 경우
    if book.stock < 1:
        flash("현재 빌릴 수 있는 재고가 없습니다. 죄송합니다.")
        return redirect(url_for('main.book_detail', id=id))

    if RentalService.is_user_rented_book(current_user.id, book.id):
        flash("이미 이 책을 빌리셨습니다.")
        return redirect(url_for('main.book_detail', id=id))

    rental = RentalService.add_rental(
        current_user.id, book.id, current_app.config["BOOK_DURATION"])

    BookService.decrease_stock(book.id)

    flash(f"{book.book_name} 책을 빌리셨습니다.")
    flash(f"반드시 {format_datetime(rental.duration)} 까지 반납해주세요!")
    return redirect(url_for('main.book_detail', id=id))


@main.route("/book/<int:id>/return", methods=["POST"])
@login_required
@is_exists_book()
def book_return(id):
    # 이 사람이 빌린 책인지 검증
    if RentalService.is_user_rented_book(current_user.id, id) == False:
        flash("잘못된 요청 입니다.")
        return redirect(url_for('mybook.rented_books'))

    RentalService.return_book(current_user.id, id)
    BookService.increase_stock(id)

    flash(f"책을 반납해주셔서 감사합니다.")
    return redirect(url_for('mybook.rented_books'))


@main.route("/book/<int:id>/review", methods=["POST"])
@login_required
@is_exists_book()
def book_review(id):
    # 올바른 책 번호 인지 체크
    # 책을 빌린적이 있는지.
    return ""
