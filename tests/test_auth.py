import unittest
from app.validation import password_valid_check


class TestAuth(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_password_valid_check_True(self):
        password = "Test12$@!55@"
        value = password_valid_check(password)
        EXPECTED = True
        self.assertEqual(EXPECTED, value)

    def test_password_valid_check_False(self):
        password = "FF!@#14" 
        value = password_valid_check(password)
        EXPECTED = False
        self.assertEqual(EXPECTED, value)
        
        password = "password123" 
        value = password_valid_check(password)
        EXPECTED = False
        self.assertEqual(EXPECTED, value)
        
        password = "Password123" 
        value = password_valid_check(password)
        EXPECTED = False
        self.assertEqual(EXPECTED, value)
        
        password = "dangerPassword!@#" 
        value = password_valid_check(password)
        EXPECTED = False
        self.assertEqual(EXPECTED, value)
        
        password = "dangerPassword" 
        value = password_valid_check(password)
        EXPECTED = False
        self.assertEqual(EXPECTED, value)


if __name__ == '__main__':
    unittest.main()
