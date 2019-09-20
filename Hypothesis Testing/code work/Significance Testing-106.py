## 3. Statistical significance ##

import numpy as np
import matplotlib.pyplot as plt

mean_group_a = np.mean(weight_lost_a)
print(mean_group_a)

mean_group_b = np.mean(weight_lost_b)
print(mean_group_b)

plt.hist(weight_lost_a)
plt.hist(weight_lost_b)

## 4. Test statistic ##

mean_difference = mean_group_b - mean_group_a 
print(mean_difference)

## 5. Permutation test ##

mean_difference = 2.52
print(all_values)

mean_differences = []
for i in range(1000):
    group_a = []
    group_b = []
    for i in all_values:
        rand_val = np.random.rand()
        if rand_val < 0.5:
            group_b.append(i)
        else:
            group_a.append(i)
    mean_a = np.mean(group_a)
    mean_b = np.mean(group_b)
    iteration_mean_difference = mean_b - mean_a
    
    mean_differences.append(iteration_mean_difference)
plt.hist(mean_differences)
plt.show()


## 7. Dictionary representation of a distribution ##

sampling_distribution = {}
for dif in mean_differences:
    if sampling_distribution.get(dif, False):
        sampling_distribution[dif] = sampling_distribution.get(dif) + 1
    else:
        sampling_distribution[dif] = 1
        

## 8. P value ##

frequencies = []
for key in sampling_distribution.keys():
    if key >= 2.52:
        frequencies.append(sampling_distribution[key])
p_value = sum(frequencies) / 1000