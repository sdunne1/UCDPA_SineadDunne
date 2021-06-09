# importing libraries
import pandas as pd
import numpy as np

# Read in merged dataframe csv file: df_drinks_con.csv
df_drinks_con = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\df_drinks_con.csv', sep=',', header=0)
print(df_drinks_con)

# Visualisation 1: Find the total litres of all alcohol by continent
# Subsetting columns 'continent' and 'total litres'