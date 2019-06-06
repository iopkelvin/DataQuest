## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
#Dictionary with keys = csv name, value = pd.csv_read() csv files
csv_names = [] #List with CVS file names
for i in data_files:
    word = i.split(".")[0]
    csv_names.append(word)
    data[word] = pd.read_csv("schools/"+i)
print(data["hs_directory"].shape)
print(data["hs_directory"].columns)

## 5. Exploring the SAT Data ##

sat = data["sat_results"]
print("First 5 rows of SAT dataframe:\n")
sat.head()

## 6. Exploring the Remaining Data ##

for key,value in data.items():
    print("First 5 rows of", key, ":\n", value)

## 8. Reading in the Survey Data ##

all_survey = pd.read_csv("schools/survey_all.txt", delimiter="\t", encoding="windows-1252")
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter="\t", encoding="windows-1252")
survey = pd.concat([all_survey, d75_survey], axis = 0)
survey.head()


## 9. Cleaning Up the Surveys ##

relevant_cols = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]
#New column "DBN" with "dbn" info
survey["DBN"] = survey["dbn"]
survey = survey.loc[:,relevant_cols]

## 11. Inserting DBN Fields ##

print(data["hs_directory"].shape)
data["hs_directory"]["DBN"]=data["hs_directory"]["dbn"]
print(data["hs_directory"].shape)

def lenght(y):
    x = str(y) 
    s = len(x) #s checks lenght of str. Whether need padding or not
    if s == 2:
        return x
    elif s == 1:
        return x.zfill(2) #zfill adds padding if only 1 character
    
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(lenght)

data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]
print("First few lines of DBN column:\n")
data["class_size"]["DBN"].head()

## 12. Combining the SAT Scores ##

#Converting SAT columns to numeric type
print("SAT column types before converting:")
print(data["sat_results"]["SAT Math Avg. Score"].dtype)
print(data["sat_results"]["SAT Critical Reading Avg. Score"].dtype)
print(data["sat_results"]["SAT Writing Avg. Score"].dtype)
data["sat_results"]["SAT Math Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Math Avg. Score"], errors = "coerce")
data["sat_results"]["SAT Critical Reading Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Critical Reading Avg. Score"], errors = "coerce")
data["sat_results"]["SAT Writing Avg. Score"] = pd.to_numeric(data["sat_results"]["SAT Writing Avg. Score"], errors = "coerce")
print("SAT column types after converting:")
print(data["sat_results"]["SAT Math Avg. Score"].dtype)
print(data["sat_results"]["SAT Critical Reading Avg. Score"].dtype)
print(data["sat_results"]["SAT Writing Avg. Score"].dtype)

#Adding up SAT score values/ columns into a single column "sat_results"
data["sat_results"]["sat_score"] = data["sat_results"]["SAT Math Avg. Score"] + data["sat_results"]["SAT Critical Reading Avg. Score"] + data["sat_results"]["SAT Writing Avg. Score"]
print("New SAT combined column results:")
data["sat_results"]["sat_score"].head()

## 13. Parsing Geographic Coordinates for Schools ##

import re #regular expression
#Extract function takes in a string and extracts items in parenthesis
#Takes in hs_directory's "Location 1" column and extracts latitude
def extract(string):
    coordinate = re.findall("\(.+\)", string)
    latitude = coordinate[0].split(",")[0].replace("(","")
    return latitude

#Applying function to Location column
data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(extract)
print("latitudes in new 'lat' column:")
data["hs_directory"]["lat"].head()

## 14. Extracting the Longitude ##

import re
#Function that extracts longitude from "Location 1" column
def extract_longitude(string):
    coordinate = re.findall("\(.+\)", string)
    longitude = coordinate[0].split(",")[1].replace(")","")
    return longitude

#Applying function to Location column
data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(extract_longitude)
print("Longitudes in new 'lon' column:")
data["hs_directory"]["lon"].head()