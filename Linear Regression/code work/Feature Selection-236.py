## 1. Missing Values ##

import pandas as pd
data = pd.read_csv('AmesHousing.txt', delimiter="\t")
train = data[0:1460]
test = data[1460:]
print(train.dtypes)
numerical_train = []
for column in train.columns:
    if (train[column].dtype == 'int64') or (train[column].dtype == 'float64'):
        numerical_train.append(column)
numerical_train = train[numerical_train].drop(['PID', 'Year Built', 'Year Remod/Add', 'Garage Yr Blt', 'Mo Sold', 'Yr Sold'], axis=1)

null_series = numerical_train.isnull().sum()
full_cols_series = null_series[null_series==0]
print(full_cols_series)

## 2. Correlating Feature Columns With Target Column ##

train_subset = train[full_cols_series.index]
full_cols_series.index
corrs = train_subset.corr()
sorted_corrs = corrs['SalePrice'].abs().sort_values()
print(sorted_corrs)

## 3. Correlation Matrix Heatmap ##

import seaborn as sns
import matplotlib.pyplot as plt
strong_corrs = sorted_corrs[sorted_corrs > .3]
corrmat = train_subset[strong_corrs.index].corr()
sns.heatmap(corrmat)

## 4. Train And Test Model ##

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

final_corr_cols = strong_corrs.drop(['Garage Cars', 'TotRms AbvGrd'])
features = final_corr_cols.drop(['SalePrice']).index
target = 'SalePrice'
clean_test = test[final_corr_cols.index].dropna()

lr = LinearRegression()
lr.fit(train[features], train[target])

train_rmse = np.sqrt(mean_squared_error(lr.predict(train[features]), train[target]))
prediction = lr.predict(clean_test[features])
test_rmse = np.sqrt(mean_squared_error(prediction, clean_test[target]))

## 5. Removing Low Variance Features ##

unit_train = (train[features] - train[features].min())/(train[features].max() - train[features].min())
print(unit_train.max())
print(unit_train.min())

sorted_vars = unit_train.var().sort_values()
print(sorted_vars)

## 6. Final Model ##

clean_test = test[final_corr_cols.index].dropna()
features = features.drop('Open Porch SF')

lr = LinearRegression()
lr.fit(train[features], train['SalePrice'])

train_predictions = lr.predict(train[features])
test_predictions = lr.predict(clean_test[features])

train_rmse_2 = np.sqrt(mean_squared_error(train_predictions, train['SalePrice']))
test_rmse_2 = np.sqrt(mean_squared_error(test_predictions, clean_test['SalePrice']))

print(train_rmse_2)
print(test_rmse_2)