## 3. Exploring the Data ##

import pandas as pd

avengers = pd.read_csv("avengers.csv")
avengers.head(5)

## 4. Filtering Out Bad Data ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame()

avengers['Year'].hist()
true_avengers = avengers[avengers["Year"]>1960]

## 5. Consolidating Deaths ##

columns = true_avengers.columns
death_cols = []
for i in list(columns):
    if i.startswith("D"):
        death_cols.append(i)
    
def clean_deaths(row):
    num_deaths = 0
    for d in death_cols:
        death = row[d]
        if death == "YES":
            num_deaths += 1
    return num_deaths

true_avengers['Deaths'] = true_avengers.apply(clean_deaths, axis=1)
true_avengers["Deaths"].head()
        

## 6. Verifying Years Since Joining ##

joined_accuracy_count = int()
correct_joined_years = true_avengers[true_avengers["Years since joining"]+true_avengers["Year"] == 2015]
joined_accuracy_count = len(correct_joined_years)