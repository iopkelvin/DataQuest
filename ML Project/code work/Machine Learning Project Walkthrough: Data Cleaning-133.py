## 3. Reading in to Pandas ##

import pandas as pd
loans_2007 = pd.read_csv('loans_2007.csv')
print(loans_2007.head(1))
print(loans_2007.columns.nunique())

## 5. First group of columns ##

drop_cols = ['id', 'member_id', 'funded_amnt', 'funded_amnt_inv', 
             'grade', 'sub_grade', 'emp_title', 'issue_d']
loans_2007 = loans_2007.drop(drop_cols, axis=1)

## 7. Second group of features ##

drop_cols = ['zip_code', 'out_prncp', 'out_prncp_inv', 'total_pymnt', 'total_pymnt_inv', 'total_rec_prncp']
loans_2007 = loans_2007.drop(drop_cols, axis=1)
             
             

## 9. Third group of features ##

drop_cols = ['total_rec_int', 'total_rec_late_fee', 'recoveries', 'collection_recovery_fee', 'last_pymnt_d', 'last_pymnt_amnt']
loans_2007 = loans_2007.drop(drop_cols, axis=1)
print(loans_2007.head(1))
print(loans_2007.columns.nunique())

## 10. Target column ##

print(loans_2007.loan_status.value_counts(normalize=True)*100)

## 12. Binary classification ##

loans_2007 = loans_2007[(loans_2007['loan_status'] == 'Fully Paid') | (loans_2007['loan_status'] == 'Charged Off')]
mapping = {'loan_status': {'Fully Paid': 1, 'Charged Off':0}}
loans_2007 = loans_2007.replace(mapping)

## 13. Removing single value columns ##

drop_columns = []
for col in loans_2007.columns:
    non_na = loans_2007[col].dropna()
    unique_num = len(non_na.unique())
    if unique_num == 1:
        drop_columns.append(col)
loans_2007 = loans_2007.drop(drop_columns, axis=1)
print(drop_columns)