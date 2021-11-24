from app.services import ReviewService
from flask import jsonify, request

from . import api


@api.route("/review", methods=["POST"])
def index():

    post_data = request.get_json()

    print(post_data)

    return jsonify(post_data)
