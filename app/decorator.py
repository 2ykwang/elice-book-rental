from functools import wraps

from flask import abort, flash, redirect, url_for

from app.services import BookService


def is_exists_book(param="id", redirect_endpoint: str = ""):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            book_id = kwargs[param]
            valid = True

            if BookService.get_book_by_id(book_id) is None:
                flash("존재하지 않는 책 id 입니다.")
                valid = False

            if not valid:
                if len(redirect_endpoint) > 0:
                    return redirect(url_for(redirect_endpoint))
                else:
                    abort(404)

            return func(*args, **kwargs)

        return decorated_function

    return decorator
