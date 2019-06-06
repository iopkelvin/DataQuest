## 3. Condensing the Class Size Data Set ##

class_size = data["class_size"] #Contains class_size dataset
class_size = class_size[class_size["GRADE "] == "09-12"] #Filtering DB so that it only contains "09-12" GRADE values
class_size = class_size[class_size["PROGRAM TYPE"] == "GEN ED"] #Filtering DB so that it only contains "GEN ED" PROGRAM TYPE values
class_size.head()



## 5. Computing Average Class Sizes ##

import numpy as np
class_size = class_size.groupby("DBN").agg(np.mean)
class_size.reset_index(inplace = True) #resets back to numerical index
data["class_size"] = class_size
data["class_size"].head(3)


## 7. Condensing the Demographics Data Set ##

data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]
data["demographics"].head(3)

## 9. Condensing the Graduation Data Set ##

data["graduation"] = data["graduation"][data["graduation"]["Cohort"] == "2006"]
#Filtering by "Total Cohort" values inn Demographic column
data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]
data["graduation"].head(3)
data["graduation"].shape

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for col in cols:
    data["ap_2010"][col] = pd.to_numeric(data["ap_2010"][col], errors="coerce")
    print(col, "type is: ", data["ap_2010"][col].dtypes)
print(data["ap_2010"].shape)

## 12. Performing the Left Joins ##

combined = data["sat_results"]
print(combined.shape)
combined = combined.merge(data["ap_2010"], how="left", on="DBN")
print(combined.shape)
combined = combined.merge(data["graduation"], how="left", on="DBN")
combined.head()
combined.shape

## 13. Performing the Inner Joins ##

#class_size
combined = combined.merge(data["class_size"], how="inner", on="DBN")
print(combined.shape)
#demographics
combined = combined.merge(data["demographics"], how="inner", on="DBN")
print(combined.shape)
#survey
combined = combined.merge(data["survey"], how="inner", on="DBN")
print(combined.shape)
#hs_directory
print(data["hs_directory"].shape)
           
combined = combined.merge(data["hs_directory"], how="inner", on="DBN")
combined.head()
print(combined.shape)

## 15. Filling in Missing Values ##

#Mean of each column
mean = combined.mean()
#Filling missing values back to combined
combined = combined.fillna(mean)
#Filling REMAINING missing values with 0
combined = combined.fillna(0)
combined.head(3)

## 16. Adding a School District Column for Mapping ##

#Function that returns first two characters of a string
def first_two(string):
    return string[0:2]
#Applying first_two function to DBN column in combined.
#New column "school_dist" has the resulting info
combined["school_dist"] = combined["DBN"].apply(first_two)
combined["school_dist"].head()