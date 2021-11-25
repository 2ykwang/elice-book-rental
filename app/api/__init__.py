from flask import Blueprint, jsonify, request
from flask_restx import Api, Namespace, Resource

blueprint = Blueprint("api", __name__)
api = Api(blueprint)

# namespaces

from .books import book_api

api.add_namespace(book_api, path="/books")
