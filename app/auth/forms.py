from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, validators
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(FlaskForm):
    # Todo: 한글이름, 영문이름 체크 정규표현식
    name = StringField('userid', validators=[DataRequired("이름을 입력해주세요."), validators.Regexp(
        regex='[가-힣a-zA-Z]+', message="이름은 한글과 영문만 가능합니다.")])
    
    email = StringField('username', validators=[DataRequired(
        "이메일을 입력해주세요."), validators.Email("올바른 형식의 이메일을 입력해주세요.")])
    # Todo: password check
    password = PasswordField('password', validators=[DataRequired(
        "비밀번호를 입력해주세요."), EqualTo('re_password', "비밀번호는 동일해야 합니다.")])
    
    re_password = PasswordField('re_password', validators=[
                                DataRequired("동일한 비밀번호를 입력해주세요.")])
