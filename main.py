# importing libraries
import pandas as pd
import numpy as np

# Read in my .csv file
pd.set_option("display.max_rows", 200, "display.max_columns", 5)
drinks = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\drinks.csv')

# First view of my dataset
print(drinks.head())

# Finding any null values & replacing with zero.
print(drinks.isnull().values.sum())
drinks = drinks.replace(np.NaN, 0)

# Checking dataframe to ensure replace was successful.
print(drinks.isnull().values.sum())

# Looking for duplicate records
dup = drinks.duplicated().any()
print(dup)

# Renaming the columns for easiness to work with.
# Checking the column names updated
drinks = drinks.rename(columns={'beer_servings': 'beer', 'wine_servings': 'wine',
                       'spirit_servings': 'spirit', 'total_litres_of_pure_alcohol': 'total_litres'}, inplace=True)

# need to fix above rename statement, and then correct sort values below.
print(drinks)

# Setting df index column.
drinks.set_index("country")

# Sorting my dataframe by country with highest total litres alcohol pp/py
drinks.sort_values('total_litres_of_pure_alcohol', ascending=False)

# Adding a new column to dataframe named continent,using merge and matching on country.
# Read in 2nd data set .csv file
country_con = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\continents.csv')

# Merging datasets drinks and country_con
# drinks_con = pd.merge()