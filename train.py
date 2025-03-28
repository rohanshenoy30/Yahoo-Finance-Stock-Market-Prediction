import matplotlib.pyplot as plt
import wandb
from wandb.keras import WandbCallback
from dataload import load_data
from model import build_model

# Initialize W&B
wandb.init(project="yahoo-stock-lstm", name="LSTM-Training", config={
    "epochs": 20,
    "batch_size": 32,
    "time_steps": 50,
    "hidden_units": 50,
    "optimizer": "adam",
    "loss_function": "mean_squared_error"
})

# Load dataset
X_train, X_test, y_train, y_test, scaler, dates = load_data("yahoo_data.xlsx")

# Build model
model = build_model()

# Train model
history = model.fit(
    X_train, y_train, 
    epochs=wandb.config.epochs, 
    batch_size=wandb.config.batch_size, 
    validation_data=(X_test, y_test), 
    callbacks=[WandbCallback()]
)

# Save model
model.save("lstm_model.h5")

# Plot training loss
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.legend()
plt.title("LSTM Training Loss")
plt.savefig("training_loss.png")
wandb.log({"Training Loss Plot": wandb.Image("training_loss.png")})
plt.show()

# Finish W&B logging
wandb.finish()
