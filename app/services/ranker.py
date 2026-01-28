from app.services.rules import rule_filter
from app.services.features import build_features
from app.services.ml_model import predict

def rank_best_place(user_lat, user_lng, places, model):
    """
    Tüm listeyi döndürmez.
    Sadece EN İYİ yeri hesaplayıp döner.
    """

    best_place = None
    best_score = float("-inf")

    # 1️⃣ kurallarla filtrele
    filtered_places = rule_filter(user_lat, user_lng, places)

    # 2️⃣ tek geçişte en iyiyi bul
    for place in filtered_places:
        features = build_features(place)
        score = predict(model, features)

        if score > best_score:
            best_score = score
            place["score"] = score
            place["features"] = features
            best_place = place

    return best_place
