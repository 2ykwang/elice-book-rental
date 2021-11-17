import os
import multiprocessing

# gunicorn - configuration
wsgi_app = "run:app"

# bind = f'{os.getenv("HOST")}:{os.getenv("PORT")}'

# heroku 환경에서 worker 갯수가 많은상태로 mysql을 사용하면 max_connection 초과됨.
# workers = multiprocessing.cpu_count() * 2

# CMD gunicorn --check--config ./gunicorn.config.py
# CMD gunicorn -c ./gunicorn.config.py