from . import main
from ..models import Book
from .. import db
from flask import render_template, request, current_app


@main.route("/")
def index():
    page = request.args.get("page", default=1, type=int) 
    book_per_page = current_app.config["BOOK_PER_PAGE"]

    query = Book.query 
    pagination = query.paginate(page, book_per_page, error_out=False)
    books = pagination.items

    return render_template("book_list.html", book_list=books, pagination=pagination, enumerate=enumerate)

@main.route("/detail/<int:id>")
def book_detail(id):
      
    book = db.session.query(Book).filter(Book.id==id).first() 
    book.increase_viewer()
    return render_template("book_detail.html", book=book)
 