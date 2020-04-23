## 1. Introduction to the data ##

import pandas as pd
cars = pd.read_csv("auto.csv")
unique_regions = cars.origin.unique()
print(unique_regions)

## 2. Dummy variables ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)

dummy_years = pd.get_dummies(cars['year'], prefix='year')
cars = pd.concat([cars, dummy_years], axis=1)

cars = cars.drop(['year', 'cylinders'], axis=1)
print(cars.head(5))


## 3. Multiclass classification ##

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]

rows_in_cars = len(shuffled_cars)

train = shuffled_cars.iloc[:int(rows_in_cars*0.7), :]
test = shuffled_cars.iloc[int(rows_in_cars*0.7):, :]

print(train.columns)

## 4. Training a multiclass logistic regression model ##

dummy_cylinders = pd.get_dummies(cars["cylinders"], prefix="cyl")
cars = pd.concat([cars, dummy_cylinders], axis=1)

dummy_years = pd.get_dummies(cars['year'], prefix='year')
cars = pd.concat([cars, dummy_years], axis=1)

cars = cars.drop(['year', 'cylinders'], axis=1)

shuffled_rows = np.random.permutation(cars.index)
shuffled_cars = cars.iloc[shuffled_rows]

rows_in_cars = len(shuffled_cars)

train = shuffled_cars.iloc[:int(rows_in_cars*0.7), :]
test = shuffled_cars.iloc[int(rows_in_cars*0.7):, :]

from sklearn.linear_model import LogisticRegression

unique_origins = cars["origin"].unique()
unique_origins.sort()

models = {}
features = [c for c in train.columns if c.startswith('cyl') or c.startswith('year')]

for i in unique_origins:
    model = LogisticRegression()
    X_train = train[features]
    y_train = train['origin'] == i
    model.fit(X_train, y_train)
    models[i] = model

## 5. Testing the models ##

testing_probs = pd.DataFrame(columns=unique_origins)
testing_probs = pd.DataFrame(columns=unique_origins)  

for origin in unique_origins:
    # Select testing features.
    X_test = test[features]   
    # Compute probability of observation being in the origin.
    testing_probs[origin] = models[origin].predict_proba(X_test)[:,1]

## 6. Choose the origin ##

predicted_origins = testing_probs.idxmax(axis=1)
print(predicted_origins)