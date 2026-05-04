import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Simple training data (weight → height)
X = np.array([[150], [160], [170], [180], [190]])
y = np.array([65, 67, 70, 72, 74])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.joblib")
print("model.joblib saved!")
