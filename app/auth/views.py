
from . import auth
from flask import render_template, redirect, request, url_for, flash

from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegisterForm
from ..models import User
from werkzeug.security import generate_password_hash, check_password_hash 

@auth.route('/', methods=['GET', 'POST'])
def index():
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    
    if request.method == 'POST': 
        if register_form.validate_on_submit(): 
            return "가입 완료"
        else:
            for message in register_form.errors.values():
                flash(str(message[-1]))
                
    return render_template('auth/register.html', form=register_form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    
    return render_template('auth/login.html')
