from .jinja_datetime import format_datetime
from .password_validation import password_valid_check
import math

from datetime import datetime
from pytz import timezone


def get_stars_count(score, max_score=10):
    return math.floor(score/max_score*5)


def korea_datetime():
    return datetime.now(timezone('Asia/Seoul'))
