
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

from . import auth
from ..validation import password_valid_check
from .forms import RegisterForm, LoginForm
from ..models import User
from .. import db
from werkzeug.security import generate_password_hash, check_password_hash


@auth.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    register_form = RegisterForm()

    if request.method == 'POST':
        if register_form.validate_on_submit():
            name = register_form.name.data
            email = register_form.email.data
            password = register_form.password.data

            if not password_valid_check(password):
                flash(f"비밀번호 형식이 잘못되었습니다. 안전한 비밀번호를 입력해주세요.")
                return render_template('auth/register.html', form=register_form)

            # 이메일 체크
            if db.session.query(User.email).filter_by(email=email).first() is not None:
                flash(f"{email} 이미 사용 중인 아이디(이메일) 입니다")
                return render_template('auth/register.html', form=register_form)

            user = User()
            user.name = name
            user.email = email
            user.set_password(password)

            db.session.add(user)
            db.session.commit()

            return render_template('auth/register_ok.html', name=name)
        else:
            for message in register_form.errors.values():
                flash(str(message[-1]))

    return render_template('auth/register.html', form=register_form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    login_form = LoginForm()

    if request.method == 'POST':
        if login_form.validate_on_submit():
            email = login_form.email.data
            password = login_form.password.data
            user = db.session.query(User).filter(User.email == email).first()

            if user is not None and user.check_password(password):
                login_user(user)
                user.update_last_login()
                return redirect(url_for('main.index'))
            else:
                flash("아이디 또는 비밀번호를 확인해주세요.")
        else:
            for message in login_form.errors.values():
                flash(str(message[-1]))

    return render_template('auth/login.html', form=login_form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))
