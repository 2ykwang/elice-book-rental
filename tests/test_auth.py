import unittest
from app.validation import password_valid_check
from app import create_app, db
from app.models import User

# sleep function
import time


class TestAuth(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app('testing')
        self.app.app_context().push()
        # db in
        db.drop_all()
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_update_last_login_expected_different(self) -> None:
        user = User("Yeonggwang", "immutable000@gmail.com", "test!2345%")
        db.session.add(user)
        db.session.commit()
        before = user.last_login

        time.sleep(0.01)
        
        user = db.session.query(User).filter(User.name == "Yeonggwang").first()
        user.update_last_login() 
        after = user.last_login
        
        # update_last_login 함수 호출 전 후 시간 비교
        self.assertNotEqual(before, after)

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
