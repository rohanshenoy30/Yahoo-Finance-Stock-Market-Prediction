import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Function to load and preprocess data
def load_data(file_path, target_col="Adj Close**", time_steps=50, test_size=0.2):
    # Load dataset
    data = pd.read_excel(file_path)

    # Convert 'Date' to datetime and sort
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.sort_values(by="Date", ascending=True)
    data.set_index("Date", inplace=True)

    # Select target column
    data = data[[target_col]]

    # Normalize data
    scaler = MinMaxScaler(feature_range=(0, 1))
    data_scaled = scaler.fit_transform(data)

    # Create sequences
    def create_sequences(data, time_steps):
        X, y = [], []
        for i in range(len(data) - time_steps):
            X.append(data[i:i+time_steps])
            y.append(data[i+time_steps])
        return np.array(X), np.array(y)

    X, y = create_sequences(data_scaled, time_steps)

    # Split into training and testing sets
    split_idx = int(len(X) * (1 - test_size))
    X_train, X_test = X[:split_idx], X[split_idx:]
    y_train, y_test = y[:split_idx], y[split_idx:]

    return X_train, X_test, y_train, y_test, scaler, data.index[-len(y_test):]

# Run only if executed directly (not when imported)
if __name__ == "__main__":
    X_train, X_test, y_train, y_test, scaler, dates = load_data("yahoo_data.xlsx")
    print(f"Train shape: {X_train.shape}, Test shape: {X_test.shape}")
