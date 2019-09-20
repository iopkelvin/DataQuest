## 2. Calculating expected values ##

males_over50k = .67 * .241 * 32561
males_under50k = .67 * .759 * 32561
females_over50k = .33 * .241 * 32561
females_under50k = .33 * .759 * 32561

## 3. Calculating chi-squared ##

observed = [6662, 1179, 15128, 9592]
expected = [5257.6, 2589.6, 16558.2, 8155.6]
values = []

for i, obs in enumerate(observed):
    exp = expected[i]
    value = (obs - exp) ** 2 / exp
    values.append(value)
    
chisq_gender_income = sum(values)

## 4. Finding statistical significance ##

import numpy as np
from scipy.stats import chisquare
expected = np.array([5257.6, 2589.6, 16558.2, 8155.6])
observed = np.array([6662, 1179, 15128, 9592])
chisq_value, pvalue_gender_income = chisquare(observed, expected)

## 5. Cross tables ##

import pandas as pd
pd.crosstab(income["sex"], [income["race"]])

## 6. Finding expected values ##

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency

observed = pd.crosstab(income["sex"], [income["race"]])
chi_val, pvalue_gender_race, df, expected = chi2_contingency(observed)
