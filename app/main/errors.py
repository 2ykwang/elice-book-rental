from . import main
from flask import render_template, url_for, flash, redirect


@main.app_errorhandler(404)
def forbidden(e):
    return render_template('errors/404.html'), 404


# 로그인 필요할 경우
@main.app_errorhandler(401)
def page_not_found(e):
    flash("로그인이 필요합니다.")
    return redirect(url_for('auth.login'))


@main.app_errorhandler(403)
def page_not_found(e):
    return render_template('errors/403.html'), 403


@main.app_errorhandler(405)
def page_not_found(e):
    return render_template('errors/405.html'), 405


@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500

# @main.app_errorhandler(Exception)
# def internal_server_error(e):
#     return render_template('errors/500.html'), 500
