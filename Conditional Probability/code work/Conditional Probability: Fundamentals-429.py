## 2. Brief Recap ##

sides = 6
p_2 = 1/sides
p_odd = 3/sides
p_2_or_4 = 2/sides

## 3. Updating Probabilities ##

less_than_5 = 4
over_5 = 0
p_3 = 1 / less_than_5
p_6 = over_5
p_odd = 2 / less_than_5
p_even = 2 / less_than_5

## 4. Conditional Probability ##

months_of_year = 12 
winter_months = 3
p_december = 1 / winter_months
p_31 = 2 / winter_months
p_summer = 0
p_ends_r = 1 / winter_months

## 5. Conditional Probability Formula ##

card_b = 6 + 5 + 4 + 3 + 2 + 1
a = 1 + 3 + 5 + 5 + 3 + 1
card_a_and_b = 9
p_a_given_b =  9 / card_b

## 6. Example Walkthough ##

hiv_neg = 30
p_negative_given_non_hiv = 6 / hiv_neg
print(p_negative_given_non_hiv)
''' This is horrible results, because we are mostly predicting positives and probably scaring people by giving them a wrong result ''' 

## 7. Probability Formula ##

p_premium_given_chrome = 158/2762
p_basic_given_safari = 274/1288
p_free_given_firefox = 2103/2285
p_premium_given_safari = 120/1288
more_likely_premium = 'Safari' 