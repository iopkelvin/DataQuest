## 1. Reading CSV Files with Encodings ##

import pandas as pd

laptops = pd.read_csv("laptops.csv", encoding = "Windows-1251")

laptops.info()

## 2. Cleaning Column Names ##

def clean(string):
    string = string.strip()
    string = string.replace("Operating System", "os")
    string = string.replace(" ", "_")
    string = string.replace("(", "")
    string = string.replace(")", "")
    string = string.lower()
    return string

columns = []
for lap in laptops.columns:
    cleaned = clean(lap)
    columns.append(cleaned)
    
laptops.columns = columns
    
    
    

## 3. Converting String Columns to Numeric ##

laptops["screen_size"] = laptops["screen_size"].str.replace('"','').astype(float)
laptops.rename({"screen_size": "screen_size_inches"}, axis=1, inplace=True)

laptops["ram"] = laptops["ram"].str.replace("GB", "")
laptops["ram"] = laptops["ram"].astype(int)
laptops.rename({"ram": "ram_gb"}, axis = 1, inplace = True)

dtypes = laptops.dtypes


## 4. Practicing Converting String Columns to Numeric ##

laptops["weight"] = laptops["weight"].str.replace("kg", "")
laptops["weight"] = laptops["weight"].str.replace("s", "")
laptops["weight"] = laptops["weight"].astype(float)
laptops.rename({"weight": "weight_kg"}, axis = 1, inplace = True)

laptops["price_euros"] = laptops["price_euros"].str.replace(",",".")
laptops["price_euros"] = laptops["price_euros"].astype(float)

weight_describe = laptops["weight_kg"].describe()
price_describe = laptops["price_euros"].describe()

## 5. Extracting Values from the Start of Strings ##

laptops["gpu_manufacturer"] = (laptops["gpu"]
                                    .str.split(n=1,expand=True)
                                    .iloc[:,0]
                               )

laptops["cpu_manufacturer"] = (laptops["cpu"].str.split(n = 1, expand = True).iloc[:,0])


## 6. Extracting Values from the End of Strings ##

screen_res = laptops["screen"].str.rsplit(n=1, expand=True)
screen_res.columns = ["A", "B"]
screen_res.loc[screen_res["B"].isnull(), "B"] = screen_res["A"]
laptops["screen_resolution"] = screen_res["B"]

 

laptops["cpu_speed_ghz"] = (laptops["cpu"].str.replace("GHz", "").str.rsplit(n=1, expand = True).iloc[:,1].astype(float))

## 7. Correcting Bad Values ##

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops["os"] = laptops["os"].map(mapping_dict)

## 8. Dropping Missing Values ##

laptops_no_null_rows = laptops.dropna()

laptops_no_null_cols = laptops.dropna(axis= 1)

## 9. Filling Missing Values ##

value_counts_before = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()
laptops.loc[laptops["os"] == "macOS", "os_version"] = "X"

laptops.loc[laptops["os"] == "No OS", "os_version"] = "Version Unknown"

value_counts_after = laptops.loc[laptops["os_version"].isnull(), "os"].value_counts()


## 10. Challenge: Extracting Storage Information ##

laptops["storage"] = laptops["storage"].str.replace("GB", "").str.replace("TB", "000")

laptops[["storage_1", "storage_2"]] = laptops["storage"].str.split("+", expand = True)

laptops[["storage_1_capacity_gb", "storage_1_type"]] = laptops["storage_1"].str.split(n=1, expand = True)
laptops[["storage_2_capacity_gb", "storage_2_type"]] = laptops["storage_2"].str.split(n=1, expand = True)

laptops["storage_1_capacity_gb"] = laptops["storage_1_capacity_gb"].astype(float)
laptops["storage_2_capacity_gb"] = laptops["storage_2_capacity_gb"].astype(float)

laptops["storage_1_type"] = laptops["storage_1_type"].str.strip()

laptops["storage_2_type"] = laptops["storage_2_type"].str.strip()


laptops.drop(["storage", "storage_1", "storage_2"], axis= 1, inplace = True)

## 11. Reordering Columns and Exporting Cleaned Data ##

laptops_dtypes = laptops.dtypes
cols = ['manufacturer', 'model_name', 'category', 'screen_size_inches',
        'screen', 'cpu', 'cpu_manufacturer', 'screen_resolution', 'cpu_speed_ghz', 'ram_gb',
        'storage_1_type', 'storage_1_capacity_gb', 'storage_2_type',
        'storage_2_capacity_gb', 'gpu', 'gpu_manufacturer', 'os',
        'os_version', 'weight_kg', 'price_euros']

laptops = laptops[cols]
laptops.to_csv("laptops_cleaned.csv", index = False)

laptops_cleaned = pd.read_csv("laptops_cleaned.csv")

laptops_cleaned_dtypes = laptops_cleaned.dtypes

