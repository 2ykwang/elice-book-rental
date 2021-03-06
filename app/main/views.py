from app.decorator import is_exists_book
from app.models import Rental, User
from app.services import DEFAULT_SORT, BookService, RentalService, ReviewService
from app.utility import format_datetime
from flask import abort, current_app, flash, redirect, render_template, request
from flask.helpers import url_for
from flask_login import current_user, login_required

from . import main


@main.route("/")
def index():
    query = request.args.get("q", default="", type=str)
    page = request.args.get("page", default=1, type=int)
    sort = request.args.get("sort", default=DEFAULT_SORT, type=str)
    style = request.args.get("style", default="list", type=str)

    book_per_page = current_app.config["BOOK_PER_PAGE"]

    if query:
        pagination = BookService.search_query(query, page, book_per_page, sort)
    else:
        pagination = BookService.get_books(page, book_per_page, sort)

    books = pagination.items

    return render_template(
        "book_list_line.html" if style == "list" else "book_list.html",
        query=query,
        style=style,
        sort=sort,
        book_list=books,
        pagination=pagination,
        enumerate=enumerate,
        get_score=BookService.get_score,
    )


@main.route("/book/<int:id>")
@is_exists_book(redirect_endpoint="main.index")
def book_detail(id):

    book = BookService.get_book_by_id(id)
    BookService.increase_viewer(book.id)

    reviews = ReviewService.get_reviews_by_bookid(book.id)

    is_rented = None
    can_write_review = False

    if current_user.is_authenticated:
        # 이 사람이 이 책을 현재 대여중인 상태인지 체크 빌렸다면 반납하기 버튼 렌더링
        is_rented = RentalService.is_user_rented_book(
            current_user.id, book.id, include_returned=False
        )

        # 리뷰 작성 가능한 상태인지 체크 - 이미 리뷰를 작성했거나 또는 빌리지 않았다면 review form 비활성화
        can_write_review = (
            RentalService.is_user_rented_book(
                current_user.id, book.id, include_returned=True
            )
            and ReviewService.get_written_review(current_user.id, book.id) is None
        )

    return render_template(
        "book_detail.html",
        book=book,
        is_rented=is_rented,
        can_write_review=can_write_review,
        get_score=BookService.get_score,
        reviews=reviews,
    )


@main.route("/book/<int:id>/rent", methods=["POST"])
@login_required
@is_exists_book()
def book_rent(id):
    book = BookService.get_book_by_id(id)
    # 재고가 없을 경우
    if book.stock < 1:
        flash("현재 빌릴 수 있는 재고가 없습니다. 죄송합니다.")
        return redirect(url_for("main.book_detail", id=id))

    if RentalService.is_user_rented_book(current_user.id, book.id):
        flash("이미 이 책을 빌리셨습니다.")
        return redirect(url_for("main.book_detail", id=id))

    rental = RentalService.add_rental(
        current_user.id, book.id, current_app.config["BOOK_DURATION"]
    )

    BookService.decrease_stock(book.id)

    flash(f"{book.book_name} 책을 빌리셨습니다.")
    flash(f"반드시 {format_datetime(rental.duration)} 까지 반납해주세요!")
    return redirect(url_for("mybook.rented_books", id=id))


@main.route("/book/<int:id>/return", methods=["POST"])
@login_required
@is_exists_book()
def book_return(id):
    # 이 사람이 빌린 책인지 검증
    if not RentalService.is_user_rented_book(current_user.id, id):
        flash("잘못된 요청 입니다.")
        return redirect(url_for("mybook.rented_books"))

    RentalService.return_book(current_user.id, id)
    BookService.increase_stock(id)

    flash("책을 반납해주셔서 감사합니다.")
    flash("책에대한 소감을 작성해주세요!")
    return redirect(url_for("main.book_detail", id=id))


@main.route("/book/<int:id>/review", methods=["POST"])
@login_required
@is_exists_book()
def book_review(id):
    action = request.form.get("act", type=str)

    if action == "write":
        content = request.form.get("content", type=str)
        score = request.form.get("score", type=int)

        # 점수가 숫자형식인지
        if not type(score) == int:
            flash("점수를 매겨주세요..!")
            return redirect(url_for("main.book_detail", id=id))

        # 1~5 범위인지
        if score > 5 or score < 1:
            flash("점수를 매겨주세요..!")
            return redirect(url_for("main.book_detail", id=id))

        # 빌렸던 적이 있는 책인지 ( 빌린사람만 리뷰를 쓸 수 있게 )
        if not RentalService.is_user_rented_book(
            current_user.id, id, include_returned=True
        ):
            flash("책을 먼저 읽고 후기를 남겨주세요!")
            return redirect(url_for("main.book_detail", id=id))

        # 이미 작성한 리뷰가 있는지
        if ReviewService.get_written_review(current_user.id, id):
            flash("이미 리뷰를 작성했어요..")
            return redirect(url_for("main.book_detail", id=id))

        ReviewService.add_review(current_user.id, id, current_user.name, content, score)
        return redirect(url_for("main.book_detail", id=id))

    elif action == "delete":
        review_id = request.form.get("review_id", type=int)

        # 리뷰삭제를 요청한 사람과 삭제할 리뷰 작성자가 일치할 경우에만
        if ReviewService.is_own_review(current_user.id, review_id):
            # 리뷰 삭제
            if not ReviewService.delete_review(review_id):
                flash("리뷰를 삭제할 수 없습니다.")
        else:
            # 다른사람의 리뷰 삭제 요청
            abort(400)

        return redirect(url_for("main.book_detail", id=id))

    else:
        # 알수없는 action
        abort(400)
