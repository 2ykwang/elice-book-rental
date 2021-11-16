from . import main
from ..models import Book
@main.route("/")
def index():
    return "Test Page"