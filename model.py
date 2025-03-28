from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Function to build LSTM model
def build_model(time_steps=50):
    model = Sequential([
        LSTM(units=50, return_sequences=True, input_shape=(time_steps, 1)),
        LSTM(units=50, return_sequences=False),
        Dense(units=25),
        Dense(units=1)  # Output layer
    ])

    # Compile model
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Run only if executed directly
if __name__ == "__main__":
    model = build_model()
    model.summary()
