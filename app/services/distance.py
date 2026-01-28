import math
from typing import Union

Number = Union[int, float]

def haversine_distance(
    lat1: Number,
    lng1: Number,
    lat2: Number,
    lng2: Number
) -> float:
    """
    İki koordinasyon arasındaki mesafeyi km cinsinden döner.
    """
    # Güvenlik
    for v in (lat1, lng1, lat2, lng2):
        if not isinstance(v, (int, float)):
            raise ValueError("Latitude/Longitude sayısal olmalı")

    R = 6371.0  # Dünya yarıçapı (km)

    d_lat = math.radians(lat2 - lat1)
    d_lng = math.radians(lat2 - lat1)

    a = (
        math.sin(d_lat / 2) ** 2
        + math.cos(math.radians(lat1))
        * math.cos(math.radians(lat2))
        * math.sin(d_lng / 2) ** 2
    )

    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
