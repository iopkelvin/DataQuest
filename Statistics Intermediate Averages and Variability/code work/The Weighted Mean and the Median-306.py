## 1. Introduction ##

mean_new = houses_per_year["Mean Price"].mean()
mean_original = sum(houses.SalePrice) / len(houses.SalePrice)
difference = mean_original - mean_new

## 2. Different Weights ##

houses_per_year["sum_per_year"] = houses_per_year["Mean Price"] * houses_per_year["Houses Sold"]
weighted_mean = houses_per_year["sum_per_year"].sum() / houses_per_year["Houses Sold"].sum()
mean_original = sum(houses["SalePrice"]) / len(houses["SalePrice"])
difference = round(mean_original, 10) - round(weighted_mean, 10)

## 3. The Weighted Mean ##

import numpy as np

def weighted_mean(distribution, weights):
    weighted_sum = []
    for mean, weight in zip(distribution, weights):
        weighted_sum.append(mean * weight)
      
    return sum(weighted_sum) / sum(weights)

weighted_mean_function = weighted_mean(houses_per_year["Mean Price"], houses_per_year["Houses Sold"])

from numpy import average
weighted_mean_numpy = average(houses_per_year["Mean Price"], weights = houses_per_year["Houses Sold"])

equal = round(weighted_mean_function, 10) == round(weighted_mean_numpy, 10)


## 4. The Median for Open-ended Distributions ##

distribution1 = [23, 24, 22, '20 years or lower,', 23, 42, 35]
distribution2 = [55, 38, 123, 40, 71]
distribution3 = [45, 22, 7, '5 books or lower', 32, 65, '100 books or more']
median1 = 23
median2 = 55
median3 = 32

## 5. Distributions with Even Number of Values ##

values = houses["TotRms AbvGrd"].copy()
sorted_values = values.replace("10 or more", 10).astype(int).sort_values(ascending=True)
median = sorted_values.iloc[int(len(sorted_values)/2)]

## 6. The Median as a Resistant Statistic ##

houses["Lot Area"].plot.box()
houses["SalePrice"].plot.box()
median_lot = houses["Lot Area"].median()
mean_lot = houses["Lot Area"].mean()
median_price = houses["SalePrice"].median()
mean_price = houses["SalePrice"].mean()
lotarea_difference = mean_lot - median_lot
saleprice_difference = mean_price - median_price



## 7. The Median for Ordinal Scales ##

mean = houses["Overall Cond"].mean()
median = houses["Overall Cond"].median()
more_representative = "mean"