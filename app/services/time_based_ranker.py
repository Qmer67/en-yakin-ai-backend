from app.services.rules import rule_filter
from app.services.time_aware_ranker import time_aware_score

def get_best_place_by_time(user_lat, user_lng, places):
    best_place = None
    best_score = float("-inf")

    valid_places = rule_filter(user_lat, user_lng, places)

    for place in valid_places:
        score = time_aware_score(place)

        if score > best_score:
            best_score = score
            best_place = place

    return best_place
