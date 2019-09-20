## 2. The Mean ##

distribution = [0,2,3,3,3,4,13]
mean = sum(distribution)/len(distribution)
center = mean == (sum(range(13))/2)
above = []
below = []

for value in distribution:
    if value < mean:
        below.append(mean - value)
    if value > mean:
        above.append(value - mean)
        
equal_distances = (sum(above) == sum(below))

## 3. The Mean as a Balance Point ##

 from numpy.random import randint, seed
equal_distances = 0
for i in range(0,5000):
    seed(i)
    intr = randint(0,1000,10)
    mean = intr.mean()
    
    above = []
    below = []
    

    for value in intr:
        if value == mean:
            continue
        if value < mean:
            below.append(mean - value)
        if value > mean:
            above.append(value - mean)
            
    above = round(sum(above), 1)
    below = round(sum(below), 1)
    if above == below:
        equal_distances += 1 
        
    

## 4. Defining the Mean Algebraically ##

one = False
two = False
three = False

## 5. An Alternative Definition ##

distribution_1 = [42, 24, 32, 11]
distribution_2 = [102, 32, 74, 15, 38, 45, 22]
distribution_3 = [3, 12, 7, 2, 15, 1, 21]

def mn(array):
    sums = 0
    for i in array:
        sums += i
    return sums/len(array)    
mean_1 = mn(distribution_1)
mean_2 = mn(distribution_2)
mean_3 = mn(distribution_3)

  

## 6. Introducing the Data ##

import pandas as pd
houses = pd.read_csv("AmesHousing_1.txt", sep='\t')
one=True
two=False
three=True


## 7. Mean House Prices ##

def mean(distribution):
    sum_distribution = 0
    for value in distribution:
        sum_distribution += value
        
    return sum_distribution / len(distribution)

function_mean = mean(houses.SalePrice)
pandas_mean = houses["SalePrice"].mean()
means_are_equal = function_mean == pandas_mean

## 8. Estimating the Population Mean ##

sample_size = 5
sampling_sizes = []
sampling_errors = []

for i in range(101):
    sample = houses["SalePrice"].sample(sample_size, random_state=i)
    sample_mean = sample.mean()
    sampling_error = houses.SalePrice.mean() - sample_mean
    sampling_errors.append(sampling_error)
    sampling_sizes.append(sample_size)
    sample_size += 29

import matplotlib.pyplot as plt
plt.scatter(x=sampling_sizes, y=sampling_errors)
plt.axhline(0)
plt.axvline(2930)
plt.xlabel("Sample size")
plt.ylabel("Sampling error")

## 9. Estimates from Low-Sized Samples ##

sample_means = []
for i in range(10000):
    sample = houses.SalePrice.sample(100, random_state=i)
    sample_mean = sample.mean()
    sample_means.append(sample_mean)
    
plt.hist(sample_means)
plt.axvline(houses.SalePrice.mean())
plt.xlabel("Sample mean")
plt.ylabel("Frequency")
plt.xlim (0,500000)

## 11. The Sample Mean as an Unbiased Estimator ##

import numpy as np
population = [3, 7, 2]
population_mean = sum(population)/len(population)
sample_means = []
for i in population:
    for j in population:
        sample_means.append((i+j)/2)
sample_means = sum(sample_means)/len(sample_means)        
unbiased = sample_means == population_mean