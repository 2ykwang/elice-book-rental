import os
import multiprocessing

# gunicorn - configuration
wsgi_app = "run:app"

# bind = f'{os.getenv("HOST")}:{os.getenv("PORT")}'
workers = multiprocessing.cpu_count() * 2

# CMD gunicorn --check--config ./gunicorn.config.py
# CMD gunicorn -c ./gunicorn.config.py