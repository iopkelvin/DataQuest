import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression

data = pd.read_csv('sphist.csv')
# Converting to datetime type
data['Date'] = pd.to_datetime(data['Date'])
# Filtering to date after 2015-04-01
# mask = data['Date'] > datetime(year=2015, month=4, day=1)
# print('shape before: ', data.shape)
# data_after = data[mask]
# print('shape after: ', data_after.shape)
# data_after
data = data.sort_values(by=['Date'], ascending=True)
# Creating indicators
data['5 Days Open'] = data['Open'].rolling(center=False, window=5).mean()
data['5 Days High'] = data['High'].rolling(center=False, window=5).mean()
data['5 Days Low'] = data['Low'].rolling(center=False, window=5).mean()
data['5 Days Volume'] = data['Volume'].rolling(center=False, window=5).mean()
# Rolling doesnt shift time
data['5 Days Open'] = data['5 Days Open'].shift(1)
data['5 Days High'] = data['5 Days High'].shift(1)
data['5 Days Low'] = data['5 Days Low'].shift(1)
data['5 Days Volume'] = data['5 Days Volume'].shift(1)
# Year column from dataframe
data['Year'] = data['Date'].apply(lambda x:x.year)
data['Day_of_week'] = data['Date'].apply(lambda x:x.weekday())
dow_dummies = pd.get_dummies(data["Day_of_week"])
data = pd.concat([data, dow_dummies], axis=1)
data = data.drop(['Day_of_week'], axis=1)

# Filter 365 Days
data = data[data['Date'] >= datetime(year=1951, month=1, day=3)]
# Remove rows with null values
data = data.dropna(axis=0)

# Generate train and test dataframe
train = data[data['Date'] < datetime(year=2013, month=1, day=1)]
test = data[data['Date'] >= datetime(year=2013, month=1, day=1)]

# Fit model
lr = LinearRegression()
# Features used to predict label
features = ['5 Days Open', '5 Days Volume', '5 Days High', '5 Days Low', 'Year', 0, 1, 2, 3, 4]

lr.fit(train[features], train['Close'])
prediction = lr.predict(test[features])

mae = mean_absolute_error(prediction, test['Close'])

print(mae)
