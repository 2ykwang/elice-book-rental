from . import main
from ..models import Book
from flask import render_template, request, current_app


@main.route("/")
def index():
    page = request.args.get("page", default=1, type=int) 
    book_per_page = current_app.config["BOOK_PER_PAGE"]

    query = Book.query
    pagination = query.paginate(page, book_per_page, error_out=False)
    books = pagination.items
    print(pagination)

    return render_template("book_list.html", book_list=books, pagination=pagination)

@main.route("/detail/<int:id>")
def book_detail(id):
     
    query = Book.query
    book = query.filter(Book.id == id).one()
    return render_template("book_detail.html", book=book)
 