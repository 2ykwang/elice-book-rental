from . import main
from ..models import Book
from flask import render_template

@main.route("/")
def index():
    return render_template("book_list.html")