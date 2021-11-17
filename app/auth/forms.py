from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    # Todo: 한글이름, 영문이름 체크 정규표현식
    name = StringField('name', validators=[
        DataRequired("이름을 입력해주세요."),
        validators.Regexp(regex='[가-힣a-zA-Z]+', message="이름은 한글과 영문만 가능합니다.")])

    email = StringField('email', validators=[
        DataRequired("이메일을 입력해주세요."),
        validators.Email("올바른 형식의 이메일을 입력해주세요.")])

    # Todo: password check
    password = PasswordField('password', validators=[
        DataRequired("비밀번호를 입력해주세요."),
        validators.Length(
            min=10, message="패스워드는 최소 10자리 이상 영어 대소문자 숫자 특수문자 조합으로 입력해주세요."),
        EqualTo('re_password', "비밀번호는 동일해야 합니다.")])

    re_password = PasswordField('re_password', validators=[
        DataRequired("동일한 비밀번호를 입력해주세요.")])


class LoginForm(FlaskForm): 
    email = StringField('email', validators=[
        DataRequired("이메일을 입력해주세요."),
        validators.Email("올바른 형식의 이메일을 입력해주세요.")])

    password = PasswordField('password', validators=[
        DataRequired("비밀번호를 입력해주세요.")])
                             
