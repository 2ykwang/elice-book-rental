import re


def password_valid_check(password: str):
    """패스워드 유효성을 확인합니다.

    Args:
        password (str): 검사할 패스워드 문자열
    """
    if (
        len(password) < 10
        or not re.findall("[a-z]+", password)
        or not re.findall("[A-Z]+", password)
        or not re.findall("[0-9]+", password)
        or not re.findall("[`~!@#$%^&*(),<.>/?]+", password)
    ):
        return False
    return True
