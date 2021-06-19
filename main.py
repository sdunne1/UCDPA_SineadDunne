# importing libraries
import pandas as pd
import numpy as np
from kaggle.api.kaggle_api_extended import KaggleApi
import csv

# Using an API token in a json file located in C:\Windows\s_dun\.kaggle.
# API Authentication using kaggle account credentials to retrieve the dataset.
api = KaggleApi()
api.authenticate()

# downloading from kaggle.com/c8debreaker619/alcohol-comsumption-around-the-world
# Writing the dataset file to my current project directory path with './'
api.dataset_download_file('codebreaker619/alcohol-comsumption-around-the-world', file_name='drinks.csv')

# Read in my .csv file, setting index column.
pd.set_option("display.max_rows", 200, "display.max_columns", 5)
df_drinks = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\drinks.csv', header=0,
                        names=['COUNTRY', 'BEER', 'SPIRIT', 'WINE', 'TOTAL_LITRES'])

# Ensure column names are updated correctly by displaying them out in a list.
for col in df_drinks.columns:
    print(col)

# First view of my dataset
print(df_drinks.head())

# Finding any null values & replacing with zero.
print(df_drinks.isnull().values.sum())
df_drinks = df_drinks.replace(np.NaN, 0)

# Checking dataframe to ensure replace was successful.
print(df_drinks.isnull().values.sum())

# Looking for duplicate records.
dup = df_drinks.duplicated().any()
print(dup)

# Sorting my dataframe by country with highest total litres alcohol pp/py
df_drinks.sort_values('TOTAL_LITRES', ascending=False)

# Setting index for dataframe df_drinks
df_drinks.set_index('COUNTRY')

# Adding a new column to dataframe named continent,using merge and matching on country.
# Read in 2nd data set .csv file
pd.set_option("display.max_rows", 200, "display.max_columns", 5)
dict_countrycon = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\continents.csv', header=0).to_dict()

# Print my keys and values from the dict_countrycon dictionary
for key, value in dict_countrycon.items():
    print(key, value)

# Converting my dictionary to a dataframe
df_countrycon = pd.DataFrame.from_dict(dict_countrycon)
print(df_countrycon.head(4))

df_countrycon.columns= df_countrycon.columns.str.upper()

# Merging datasets drinks and country_con
df_drinks_con = pd.merge(df_drinks, df_countrycon, on='COUNTRY', how='left')
df_drinks_con.set_index('COUNTRY')
print(df_drinks_con.head(4))




# Downloading cleaned dataframe as csv file to import into drinks_viz.py
df_drinks_con.to_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\df_drinks_con.csv', index=False, sep=',', header=True)



