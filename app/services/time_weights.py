from typing import Dict

TimeWeight = Dict[str, float]

TIME_WEIGHTS: Dict[str, TimeWeight] = {
    "morning": {
        "distance": 0.5,
        "rating": 0.2,
        "price": 0.3
    },
    "noon": {
        "distance": 0.3,
        "rating": 0.5,
        "price": 0.2
    },
    "evening": {
        "distance": 0.2,
        "rating": 0.6,
        "price": 0.2
    },
    "night": {
        "distance": 0.6,
        "rating": 0.3,
        "price": 0.1
    }
}


def get_time_weights(segment: str) -> TimeWeight:
    """
    Güvenli ağırlık döner.
    """
    weights = TIME_WEIGHTS.get(segment, TIME_WEIGHTS["noon"])

    total = sum(weights.values())
    if abs(total - 1.0) > 0.01:
        # normalize et
        return {k: v / total for k, v in weights.items()}

    return weights
