## 1. Recap ##

import pandas as pd
loans = pd.read_csv('cleaned_loans_2007.csv')
print(loans.info())

## 3. Picking an error metric ##

import pandas as pd
tn = len(predictions[(predictions==0) & (loans['loan_status']==0)])
tp = len(predictions[(predictions==1) & (loans['loan_status']==1)])
fn = len(predictions[(predictions==0) & (loans['loan_status']==1)])
fp = len(predictions[(predictions==1) & (loans['loan_status']==0)])

## 5. Class imbalance ##

import pandas as pd
import numpy

# Predict that all loans will be paid off on time.
predictions = pd.Series(numpy.ones(loans.shape[0]))
# False positives.
fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

# Rates
tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

print(tpr)
print(fpr)

## 6. Logistic Regression ##

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

features = loans.drop('loan_status', axis=1)
target = loans.loan_status

lr.fit(features, target)
predictions = lr.predict(features)

## 7. Cross Validation ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict
lr = LogisticRegression()
predictions = cross_val_predict(lr, features, target, cv=3)
predictions = pd.Series(predictions)

tp = len(predictions[(predictions==1)&(target==1)])
tn = len(predictions[(predictions==0)&(target==0)])
fp = len(predictions[(predictions==1)&(target==0)])
fn = len(predictions[(predictions==0)&(target==1)])

tpr = tp / (tp+fn)
fpr = fp / (fp+tn)

print(tpr)
print(fpr)

## 9. Penalizing the classifier ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict

lr = LogisticRegression(class_weight='balanced')

predictions = cross_val_predict(lr, features, target)
predictions = pd.Series(predictions)

tp = len(predictions[(predictions == 1) & (target == 1)])
tn = len(predictions[(predictions == 0) & (target == 0)])
fp = len(predictions[(predictions == 1) & (target == 0)])
fn = len(predictions[(predictions == 0) & (target == 1)])

tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

print(tpr)
print(fpr)

## 10. Manual penalties ##

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_predict

penalty = {0: 10,
          1: 1}

lr = LogisticRegression(class_weight=penalty)

predictions = cross_val_predict(lr, features, target)
predictions = pd.Series(predictions)

tp = len(predictions[(predictions == 1) & (target == 1)])
tn = len(predictions[(predictions == 0) & (target == 0)])
fp = len(predictions[(predictions == 1) & (target == 0)])
fn = len(predictions[(predictions == 0) & (target == 1)])

tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

print(tpr)
print(fpr)

## 11. Random forests ##

from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import cross_val_predict

lr = RandomForestClassifier(random_state=1, class_weight='balanced')

predictions = cross_val_predict(lr, features, target)
predictions = pd.Series(predictions)

tp = len(predictions[(predictions == 1) & (target == 1)])
tn = len(predictions[(predictions == 0) & (target == 0)])
fp = len(predictions[(predictions == 1) & (target == 0)])
fn = len(predictions[(predictions == 0) & (target == 1)])

tpr = tp / (tp + fn)
fpr = fp / (fp + tn)

print(tpr)
print(fpr)