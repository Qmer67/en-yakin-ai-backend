from fastapi import APIRouter
from pydantic import BaseModel

from app.models import BestPlaceRequest
from app.services.rules import rule_filter
from app.services.features import build_features
from app.services.ml_model import load_model, predict, update_model
from app.services.time_segment import get_time_segment
from app.services.time_weights import get_time_weights   # ✅ DEĞİŞTİ
from app.services.click_logger import log_click

router = APIRouter()

# Model tek kez yüklenir
model = load_model()


@router.post("/best-place")
def best_place(data: BestPlaceRequest):
    places = [p.dict() for p in data.places]

    # 1️⃣ Kural tabanlı filtre
    valid_places = rule_filter(
        data.user_lat,
        data.user_lng,
        places
    )

    if not valid_places:
        return {"error": "Uygun yer bulunamadı"}

    # 2️⃣ Zaman bağlamı
    time_segment = get_time_segment()
    weights = get_time_weights(time_segment)   # ✅ DEĞİŞTİ

    best_place = None
    best_score = float("-inf")

    # 3️⃣ TEK GEÇİŞTE EN İYİYİ BUL
    for place in valid_places:
        features = build_features(place)

        distance_score = 1 / (place["distance"] + 0.1)
        rating_score = place.get("rating", 0) / 5
        price_score = 1 / place.get("price_level", 3)

        time_weighted_score = (
            weights["distance"] * distance_score +
            weights["rating"] * rating_score +
            weights["price"] * price_score
        )

        # Kullanıcı davranışından öğrenen skor
        behavior_score = predict(model, features)

        # Hibrit final skor
        final_score = (
            0.5 * time_weighted_score +
            0.5 * behavior_score
        )

        if final_score > best_score:
            best_score = final_score
            place["final_score"] = final_score
            place["time_segment"] = time_segment
            place["features"] = features
            best_place = place
