## 2. Introduction To The Data ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', sep='\t')
train = data.iloc[:1460, :]
test = data.iloc[1460:, :]
target = 'SalePrice'
train.info()

## 3. Simple Linear Regression ##

import matplotlib.pyplot as plt
# For prettier plots.
import seaborn

fig = plt.figure(figsize=(7,15))
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)
train.plot('Garage Area', 'SalePrice', ax=ax1, kind='scatter')
train.plot('Gr Liv Area', 'SalePrice', ax=ax2, kind='scatter')
train.plot('Overall Cond', 'SalePrice', ax=ax3, kind='scatter')
plt.show()

## 5. Using Scikit-Learn To Train And Predict ##

from sklearn.linear_model import LinearRegression
model = LinearRegression()
features = train.iloc[:,:-1]
print(target)
model.fit(train[['Gr Liv Area']], train['SalePrice'])
a1 = model.coef_
a0 = model.intercept_



## 6. Making Predictions ##

import numpy as np

lr = LinearRegression()
lr.fit(train[['Gr Liv Area']], train['SalePrice'])

from sklearn.metrics import mean_squared_error

train_rmse = np.sqrt(mean_squared_error(
    lr.predict(train[['Gr Liv Area']]), train['SalePrice']
))
test_rmse = np.sqrt(mean_squared_error(
    lr.predict(test[['Gr Liv Area']]), test['SalePrice']
))

## 7. Multiple Linear Regression ##

cols = ['Overall Cond', 'Gr Liv Area']
lr = LinearRegression()
lr.fit(train[cols], train['SalePrice'])
train_rmse_2 = np.sqrt(mean_squared_error(lr.predict(train[cols]), train['SalePrice']))
                       
test_rmse_2 = np.sqrt(mean_squared_error(lr.predict(test[cols]), test['SalePrice']))