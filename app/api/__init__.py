from flask import Blueprint, jsonify, request
from flask_restx import Api, Namespace, Resource

blueprint = Blueprint("api", __name__)
api = Api(
    blueprint,
    version="0.1",
    title="Elice Library REST API",
    description="Hi👋,thank you for visiting this is the Elice library swagger ui documentation site",
    contact_url="https://github.com/2ykwang",
    contact_email="immutable000@gmail.com",
)

# namespaces

from .books import book_api

api.add_namespace(book_api, path="/books")


from .auth import auth_api

api.add_namespace(auth_api, path="/auth")
