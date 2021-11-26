FROM python:3.8.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD gunicorn --check--config ./gunicorn.config.py
CMD gunicorn -c ./gunicorn.config.py
