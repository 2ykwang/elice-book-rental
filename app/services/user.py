from typing import Union
from app.utility import korea_datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from app import db


class UserService(object):

    @staticmethod
    def add_user(name: str, email: str, password: str) -> User:
        hashed_password = generate_password_hash(password)
        user = User(name, email, hashed_password)
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def check_password(user_id: int, password) -> bool:
        user = db.session.query(User).filter(User.id == user_id).first()
        return check_password_hash(user.password_hash, password)
    
    @staticmethod
    def get_user_by_id(id: str) -> Union[User, None]:
        user = db.session.query(User).filter(User.id == id).first()
        return user
    
    @staticmethod
    def get_user_by_email(email: str) -> Union[User, None]:
        user = db.session.query(User).filter(User.email == email).first()
        return user

    @staticmethod
    def update_last_login(user_id: int) -> None:
        user = db.session.query(User).filter(User.id == user_id).first()
        user.last_login = korea_datetime()
        db.session.add(user)
        db.session.commit()
