from app.services.time_segment import get_time_segment
from app.services.time_weights import TIME_WEIGHTS

def time_aware_score(place):
    """
    Zaman segmentine göre skor üretir
    """
    segment = get_time_segment()
    weights = TIME_WEIGHTS[segment]

    distance_score = 1 / (place["distance"] + 0.1)
    rating_score = place.get("rating", 0) / 5
    price_score = 1 / place.get("price_level", 3)

    score = (
        weights["distance"] * distance_score +
        weights["rating"] * rating_score +
        weights["price"] * price_score
    )

    place["time_segment"] = segment
    place["time_score"] = score

    return score
