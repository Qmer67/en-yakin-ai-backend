from datetime import datetime
from app.services.distance import haversine_distance

DEFAULT_MAX_DISTANCE_KM = 5


def is_place_open(current_hour: int, open_hour: int, close_hour: int) -> bool:
    """
    Gece sarkan saatleri de doğru şekilde kontrol eder.
    Örn: 22 - 04
    """
    if open_hour <= close_hour:
        return open_hour <= current_hour <= close_hour
    else:
        # Gece taşan saatler (örn 22-04)
        return current_hour >= open_hour or current_hour <= close_hour


def rule_filter(user_lat, user_lng, places, max_distance_km: float = DEFAULT_MAX_DISTANCE_KM):
    current_hour = datetime.now().hour
    valid_places = []

    for place in places:
        distance = haversine_distance(
            user_lat,
            user_lng,
            place["lat"],
            place["lng"]
        )

        if distance > max_distance_km:
            continue

        if not place.get("is_open", True):
            continue

        open_hour = place.get("open_hour")
        close_hour = place.get("close_hour")

        if open_hour is not None and close_hour is not None:
            if not is_place_open(current_hour, open_hour, close_hour):
                continue

        place["distance"] = distance
        valid_places.append(place)

    return valid_places
