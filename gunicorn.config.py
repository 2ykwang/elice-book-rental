import multiprocessing
import os

# gunicorn - configuration
wsgi_app = "run:app"

bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 - 1
# bind = f'{os.getenv("HOST")}:{os.getenv("PORT")}'

# heroku 환경에서 worker 갯수가 많은상태로 mysql을 사용하면 max_connection 초과됨.

# CMD gunicorn --check--config ./gunicorn.config.py
# CMD gunicorn -c ./gunicorn.config.py
