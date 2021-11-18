import unittest
from app import create_app, db
from app.models import User,Rental
from fake import make_fake_book, make_fake_user 

class TestBook(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app('testing')
        self.app.app_context().push()
        db.drop_all()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove() 
        db.drop_all()

    def test_rent_book(self) -> None:
        pass
    

    def test_decrease_and_increase_book_quantity(self) -> None:
         
        book = make_fake_book() 
        book.stock = 10 
        
        db.session.add(book) 
        db.session.commit()
        
        book.decrease_stock(3)
        
        EXPECTED=7
        self.assertEqual(EXPECTED, book.stock)
        
        book.increase_stock(5)
        
        EXPECTED=12
        self.assertEqual(EXPECTED, book.stock)
         


if __name__ == '__main__':
    unittest.main()
