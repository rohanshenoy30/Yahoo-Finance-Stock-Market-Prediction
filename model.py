# Build LSTM Model
model = Sequential([
    LSTM(units=50, return_sequences=True, input_shape=(time_steps, 1)),
    LSTM(units=50, return_sequences=False),
    Dense(units=25),
    Dense(units=1)  # Output layer
])

# Compile model
model.compile(optimizer='adam', loss='mean_squared_error')

# Model summary
model.summary()
