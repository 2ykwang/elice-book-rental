import math

from datetime import datetime
from pytz import timezone


def korea_datetime():
    return datetime.now(timezone('Asia/Seoul'))


def dict_combine(t1: dict, t2: dict) -> dict:
    t1.update(t2)
    return t1

from typing import Any
from .jinja_datetime import format_datetime
from .jinja_datetime import created_datetime
from .password_validation import password_valid_check