from pydantic import BaseModel
from typing import List, Optional

class Place(BaseModel):
    id: int
    name: str
    lat: float
    lng: float

    rating: float = 0.0
    price_level: int = 3
    is_open: bool = True

    # 🔥 ZAMAN BAĞLAMI İÇİN ŞART
    open_hour: Optional[int] = None   # 0–23
    close_hour: Optional[int] = None  # 0–23

class BestPlaceRequest(BaseModel):
    user_lat: float
    user_lng: float
    places: List[Place]
