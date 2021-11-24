from flask import Blueprint

api = Blueprint("api", __name__)

from . import book, rent, review, user
