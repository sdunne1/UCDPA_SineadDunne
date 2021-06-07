# importing libraries
import pandas as pd
import numpy as np

# Read in my .csv file, setting index column.
pd.set_option("display.max_rows", 200, "display.max_columns", 5)
df_drinks = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\drinks.csv', header=0,
                        names=['COUNTRY', 'BEER', 'SPIRIT', 'WINE', 'TOTAL_LITRES'])

# Setting index for dataframe df_drinks
df_drinks.set_index('COUNTRY')

# Sorting my dataframe by country with highest total litres alcohol pp/py
df_drinks.sort_values('TOTAL_LITRES', ascending=False)

# First view of my dataset
print(df_drinks.head())

# Finding any null values & replacing with zero.
print(df_drinks.isnull().values.sum())
df_drinks = df_drinks.replace(np.NaN, 0)

# Checking dataframe to ensure replace was successful.
print(df_drinks.isnull().values.sum())

# Looking for duplicate records
dup = df_drinks.duplicated().any()
print(dup)

# Adding a new column to dataframe named continent,using merge and matching on country.
# Read in 2nd data set .csv file
pd.set_option("display.max_rows", 200, "display.max_columns", 5)
df_countrycon = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\continents.csv', header=0,
                            names=['COUNTRY', 'CONTINENT'])
print(df_countrycon)

# Merging datasets drinks and country_con
df_drinks_con = pd.merge(df_drinks, df_countrycon, on='COUNTRY', how='left')
print(df_drinks_con)
df_drinks_con.set_index('COUNTRY')