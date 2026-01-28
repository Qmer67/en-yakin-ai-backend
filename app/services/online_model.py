import joblib
import numpy as np
from sklearn.linear_model import SGDClassifier

MODEL_PATH = "online_model.pkl"

def load_or_create_model():
    try:
        return joblib.load(MODEL_PATH)
    except FileNotFoundError:
        model = SGDClassifier(
            loss="log_loss",
            learning_rate="optimal"
        )
        return model

def update_model(model, X, y):
    model.partial_fit(
        np.array(X),
        np.array(y),
        classes=[0, 1]
    )
    joblib.dump(model, MODEL_PATH)

def predict_probability(model, features):
    return model.predict_proba([features])[0][1]
