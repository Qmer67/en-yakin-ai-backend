from app.services.distance import haversine_distance

def calculate_score(user_lat, user_lng, place):
    distance = haversine_distance(
        user_lat, user_lng,
        place["lat"], place["lng"]
    )

    distance_score = 1 / (distance + 0.1)
    rating_score = place["rating"] / 5
    price_score = 1 / place["price_level"]
    open_score = 1 if place["is_open"] else 0

    final_score = (
        0.5 * distance_score +
        0.3 * rating_score +
        0.15 * price_score +
        0.05 * open_score
    )

    return final_score


def get_best_place(user_lat, user_lng, places):
    for place in places:
        place["score"] = calculate_score(user_lat, user_lng, place)

    return max(places, key=lambda x: x["score"])
