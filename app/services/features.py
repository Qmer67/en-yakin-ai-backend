from datetime import datetime
import math

def build_features(place):
    now = datetime.now()
    hour = now.hour

    # Zaman segmenti (ML için daha anlamlı)
    is_morning = 1 if 6 <= hour < 11 else 0
    is_noon = 1 if 11 <= hour < 17 else 0
    is_evening = 1 if 17 <= hour < 23 else 0
    is_night = 1 if hour >= 23 or hour < 6 else 0

    # Normalize edilmiş feature'lar
    distance = place["distance"]
    distance_norm = math.log(distance + 1)  # 0–~2

    rating_norm = place.get("rating", 0) / 5
    price_norm = place.get("price_level", 3) / 4

    weekday_norm = now.weekday() / 6

    return [
        distance_norm,
        rating_norm,
        price_norm,
        weekday_norm,
        is_morning,
        is_noon,
        is_evening,
        is_night
    ]
