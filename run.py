from app import create_app, db
from flask_migrate import Migrate, upgrade

import os
from dotenv import load_dotenv
import datetime

# load local .env
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()


@app.cli.command()
def init():
    """Initialize book list"""
    with open('docs/resource/book_list.csv', newline='') as csvfile:
        
        from app.models import Book
        from utility.book_data import books
        
        for item in books:
            book = Book()
            book.id = item[0]
            book.book_name = item[1]
            book.publisher = item[2]
            book.author = item[3]
            book.publication_date = datetime.datetime.strptime(
                item[4], '%Y-%m-%d')
            book.pages = item[5]
            book.isbn = item[6]
            book.description = item[7]
            book.link = item[8]
            book.image_url = f'images/{item[9]}'
            db.session.add(book)
            db.session.commit()
