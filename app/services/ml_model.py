import os
import joblib
import numpy as np
from threading import Lock
from sklearn.linear_model import SGDClassifier

# Dosyanın bulunduğu dizine göre path (SAFE)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "..", "model.pkl")

_model_lock = Lock()


def _create_initial_model():
    model = SGDClassifier(
        loss="log_loss",
        learning_rate="optimal"
    )
    # dummy fit (predict_proba çalışsın diye)
    model.partial_fit(
    np.array([[0, 0, 0, 0, 0, 0, 0, 0]]),
    np.array([0]),
    classes=[0, 1]
)
    return model


def load_model():
    with _model_lock:
        if not os.path.exists(MODEL_PATH):
            model = _create_initial_model()
            joblib.dump(model, MODEL_PATH)
            return model

        return joblib.load(MODEL_PATH)


def predict(model, features):
    """
    Kullanıcının bu yeri seçme olasılığı (0–1)
    """
    try:
        return model.predict_proba([features])[0][1]
    except Exception:
        # fallback (model henüz hazır değilse)
        return 0.5


def update_model(model, features, selected: bool):
    y = 1 if selected else 0

    with _model_lock:
        model.partial_fit(
            np.array([features]),
            np.array([y])
        )
        joblib.dump(model, MODEL_PATH)
