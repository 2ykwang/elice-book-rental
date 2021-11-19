import math 

def get_stars_count(score, max_score=10):
    return math.floor(score/max_score*5)
