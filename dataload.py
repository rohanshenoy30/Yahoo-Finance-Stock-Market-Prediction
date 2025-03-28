import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.metrics import mean_squared_error



data = pd.read_excel("/Users/rohanshenoy/Downloads/yahoo_data.xlsx")

data['Date'] = pd.to_datetime(data['Date'])
data=data.sort_values(by="Date",ascending=True)
data.set_index("Date",inplace=True)

print(data.head())
print(data.info())

fig = plt.figure(figsize=(25,25))
i=1
for x in data.columns :
    plt.subplot(2,3,i)
    ax=sns.lineplot(data[x])
    ax.set(xlabel=None)
    plt.title(str(x), loc='center')
    plt.xlabel(None)
    plt.ylabel(None)
    i+=1
plt.show()
