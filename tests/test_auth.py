import unittest
from app.validation import password_valid_check

# 순환 참조 주의
from app import create_app, db
from app.services.user import UserService

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
        user = UserService.add_user(
            "Yeonggwang", "immutable000@gmail.com", "test!2345%")
        before = user.last_login

        time.sleep(0.01)

        user = UserService.get_user_by_email("immutable000@gmail.com")
        UserService.update_last_login(user.id)
        after = user.last_login

        # update_last_login 함수 호출 전 후 시간 비교
        self.assertNotEqual(before, after)

    def test_password_valid_check_True(self):
        cases = [
            {"expected": True, "test_value": "232$@SafetyPassword1$28#241"},
            {"expected": True, "test_value": "elicePASWord2!@#$"},
            {"expected": True, "test_value": "@#$qweFrtyy@43248@"},
            {"expected": True, "test_value": "FEWHF*Hss@#*()H*)#@HF13()H@#(*)FH#@HJFOIH#FO@HIO"},
            {"expected": True, "test_value": "zzFzz)@#jj9j()(@J()E()"},
        ]

        for case in cases:
            password = case["test_value"]
            EXPECTED = case["expected"]
            ANSWER = password_valid_check(password)
            print(EXPECTED, ANSWER, password)
            self.assertEqual(EXPECTED, ANSWER)

    def test_password_valid_check_False(self):
        cases = [
            {"expected": False, "test_value": "FF!@#14"},
            {"expected": False, "test_value": "password123"},
            {"expected": False, "test_value": "Password123"},
            {"expected": False, "test_value": "dangerPassword!@#"},
            {"expected": False, "test_value": "dangerPassword"},
        ]

        for case in cases:
            password = case["test_value"]
            EXPECTED = case["expected"]
            ANSWER = password_valid_check(password)
            self.assertEqual(EXPECTED, ANSWER)


if __name__ == '__main__':
    unittest.main()
