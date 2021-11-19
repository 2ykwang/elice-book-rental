from .jinja_datetime import format_datetime
from .password_validation import password_valid_check
import math


def get_stars_count(score, max_score=10):
    return math.floor(score/max_score*5)
