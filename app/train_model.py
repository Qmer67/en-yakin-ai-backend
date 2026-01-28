from app.services.ml_model import train_model

X = [
    [0.2, 4.5, 2, 10, 2],
    [1.5, 3.2, 3, 21, 4],
    [0.5, 4.9, 1, 14, 1],
    [3.0, 4.0, 2, 9, 0],
]

y = [0.95, 0.3, 0.98, 0.5]

train_model(X, y)
print("✅ model.pkl oluşturuldu")
