import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_squared_error
import wandb
from dataload import load_data

# Initialize W&B
wandb.init(project="yahoo-stock-lstm", name="LSTM-Inference")

# Load dataset (without training it again)
X_train, X_test, y_train, y_test, scaler, dates = load_data("yahoo_data.xlsx")

# Load trained model
model = load_model("lstm_model.h5")

# Make predictions
y_pred = model.predict(X_test)

# Convert predictions back to original scale
y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1))
y_pred_inv = scaler.inverse_transform(y_pred)

# Compute RMSE
rmse = np.sqrt(mean_squared_error(y_test_inv, y_pred_inv))
wandb.log({"RMSE": rmse})
print(f"RMSE: {rmse:.2f}")

# Plot actual vs predicted values
plt.figure(figsize=(12, 6))
plt.plot(dates, y_test_inv, label="Actual", color='blue')
plt.plot(dates, y_pred_inv, label="Predicted", color='red')
plt.legend()
plt.title("Yahoo Stock Price Prediction with LSTM")
plt.savefig("lstm_prediction.png")
wandb.log({"LSTM Prediction Plot": wandb.Image("lstm_prediction.png")})
plt.show()

# Finish W&B logging
wandb.finish()
