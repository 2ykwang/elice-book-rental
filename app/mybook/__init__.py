from flask import Blueprint

mybook = Blueprint('mybook', __name__)

from . import views