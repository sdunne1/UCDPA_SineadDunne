# importing libraries
from typing import Dict

import pandas as pd
import numpy as np

# Read in my .csv file
pd.set_option("display.max_rows", None, "display.max_columns", None)
drinks = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\drinks.csv')

# First view of my dataset
print(drinks.head())

# Finding any null values & replacing with zero.
print(drinks.isnull().values.sum())
drinks = drinks.replace(np.NaN, 0)

# Checking dataframe to ensure replacing occurred.
print(drinks.isnull().values.sum())

# Looking for duplicate records
boolean = drinks.duplicated().any()

# Renaming the columns for easiness to work with.
# Checking the column names updated
drinks.rename(columns={'beer_servings': 'beer',
                        'wine_servings': 'wine',
                        'spirit_servings': 'spirit',
                        'total_litres_of_pure_alcohol': 'total litres'}, inplace=True)

# Sorting my dataframe to alphabetical order
drinks.sort_values("country", ascending=True)

# Adding a new column to dataframe named continent
