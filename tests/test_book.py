import unittest
from app import create_app, db

class TestBook(unittest.TestCase):
    def setUp(self) -> None: 
        app = create_app('testing')
        db.create_all()
        

    def tearDown(self) -> None:
        # db.drop_all()
        pass

    def test_decrease_quantity_when_rental(self) -> None:  
        value = True
        EXPECTED = True
        self.assertEqual(EXPECTED, value)

if __name__ == '__main__':
    unittest.main()
