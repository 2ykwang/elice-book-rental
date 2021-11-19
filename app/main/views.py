from . import main

from flask import render_template, request, current_app

from app.services import BookService 
from app.utility import get_stars_count 

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

@main.route("/detail/<int:id>")
def book_detail(id): 
    book = BookService.get_book_by_id(id)
    
    BookService.increase_viewer(book.id)
    
    return render_template("book_detail.html", 
                           book=book, 
                           get_stars_count=get_stars_count,
                           get_score=BookService.get_score)
 
  