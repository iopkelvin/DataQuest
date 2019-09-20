## 1. The Range ##

import pandas as pd
houses = pd.read_table('AmesHousing_1.txt')
def function(array):
    return max(array) - min(array)
houses.groupby("Yr Sold")
range_by_year = dict(houses.groupby("Yr Sold").agg(function)["SalePrice"])
one = False
two = True


## 2. The Average Distance ##

C = [1,1,1,1,1,1,1,1,1,21]
def function(array):
    mean = sum(array)/len(array)
    empty = []
    for i in array:
        empty.append(i - mean)
    return sum(empty)/len(empty)
avg_distance = function(C)

## 3. Mean Absolute Deviation ##

C = [1,1,1,1,1,1,1,1,1,21]
def function(array):
    mean = sum(array)/len(array)
    lists = []
    for i in array:
        lists.append(abs(i - mean))
    return sum(lists)/len(lists)

mad = function(C)


## 4. Variance ##

C = [1,1,1,1,1,1,1,1,1,21]
def function(array):
    mean = sum(array)/len(array)
    lists = []
    for i in array:
        lists.append((i - mean)**2)
    return sum(lists)/len(lists)
variance_C = function(C)

## 5. Standard Deviation ##

from math import sqrt
C = [1,1,1,1,1,1,1,1,1,21]
def standard_deviation(array):
    mean = sum(array)/len(array)
    lists = []
    for i in array:
        lists.append((i-mean)**2)
    variance = sum(lists)/len(lists)
    return variance**(1/2)
standard_deviation_C = standard_deviation(C)

## 6. Average Variability Around the Mean ##

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
        
    variance = sum(distances) / len(distances)
    
    return variance ** (1/2)
greatest_variability = 2006
lowest_variability = 2010

houses.groupby("Yr Sold").agg(standard_deviation)["SalePrice"]


## 7. A Measure of Spread ##

sample1 = houses['Year Built'].sample(50, random_state = 1)
sample2 = houses['Year Built'].sample(50, random_state = 2)

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return variance ** (1/2)
bigger_spread = "sample 2"
st_dev1 = standard_deviation(sample1)
st_dev2 = standard_deviation(sample2)

## 8. The Sample Standard Deviation ##

import numpy as np

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return np.sqrt(variance)

import matplotlib.pyplot as plt

deviations = []
for i in range(5000):
    sample = houses["SalePrice"].sample(10, random_state=i)
    standard = standard_deviation(sample)
    deviations.append(standard)
    
plt.hist(deviations)
plt.axvline(standard_deviation(houses["SalePrice"]))

## 9. Bessel's Correction ##

from math import sqrt
def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / len(distances)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)

pop_stdev = standard_deviation(houses['SalePrice'])
#plt.hist(st_devs)
#plt.axvline(pop_stdev)
from math import sqrt

def standard_deviation(array):
    reference_point = sum(array) / len(array)
    
    distances = []
    for value in array:
        squared_distance = (value - reference_point)**2
        distances.append(squared_distance)
    
    variance = sum(distances) / (len(distances) - 1)
    
    return sqrt(variance)

import matplotlib.pyplot as plt
st_devs = []

for i in range(5000):
    sample = houses['SalePrice'].sample(10, random_state = i)
    st_dev = standard_deviation(sample)
    st_devs.append(st_dev)
    
plt.hist(st_devs)
plt.axvline(pop_stdev)

## 10. Standard Notation ##

sample = houses.sample(100, random_state = 1)
from numpy import std, var
pandas_stdev = sample["SalePrice"].std(ddof=1)
numpy_stdev = std(sample["SalePrice"], ddof=1)
equal_stdevs = pandas_stdev == numpy_stdev

pandas_var = sample["SalePrice"].var()
numpy_var = numpy.var(sample["SalePrice"], ddof=1)
equal_vars = pandas_var == numpy_var

## 11. Sample Variance — Unbiased Estimator ##

population = [0, 3, 6]

samples = [[0,3], [0,6],
           [3,0], [3,6],
           [6,0], [6,3]
          ]
from numpy import var, std

pop_var = var(population, ddof = 0)
pop_std = std(population, ddof = 0)

st_devs = []
variances = []

for sample in samples:
    st_devs.append(std(sample, ddof = 1))
    variances.append(var(sample, ddof = 1))
    
mean_std = sum(st_devs) / len(st_devs)
mean_var = sum(variances) / len(variances)

equal_stdev = pop_std == mean_std
equal_var = pop_var == mean_var