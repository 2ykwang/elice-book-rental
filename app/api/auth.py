from app.services import UserService
from flask import current_app, request
from flask_restx import Namespace, Resource

from .errors import ERROR_VALUE_ALREADY_EXISTS
from .response import Response

auth_api = Namespace("auth", description="유저 인증 API")


# 가입
@auth_api.route("/signup")
@auth_api.doc(
    description="엘리스 도서관에 가입합니다. ( not implemented )",
    responses={
        200: "데이터 반환에 성공한 경우",
        400: "잘못된 요청일 경우",
        409: "이미 존재하는 계정일 경우",
        500: "가입에 실패 할 경우",
    },
)
class AuthSignup(Resource):
    def post(self):
        return ""


# 로그인
@auth_api.route("/signin")
@auth_api.doc(
    description="토큰키를 얻기 위해 로그인을 합니다.",
    responses={200: "데이터 반환에 성공한 경우", 400: "잘못된 요청일 경우", 500: "로그인에 실패 할 경우"},
)
class AuthSignin(Resource):
    def post(self):
        return ""


# 유저 정보
@auth_api.route("/user")
@auth_api.doc(
    description="토큰키를 얻기 위해 로그인을 합니다.",
    responses={200: "데이터 반환에 성공한 경우", 401: "유저 인증에 실패한 경우"},
)
class AuthUser(Resource):
    def get(self):
        return ""
