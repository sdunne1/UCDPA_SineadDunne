# importing libraries
import matplotlib.pyplot
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in merged dataframe csv file: df_drinks_con.csv
df_drinks_con = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\df_drinks_con.csv', sep=',', header=0)
print(df_drinks_con)

# Visualisation 1: Top 10 countries with total litres consumed per person
df = pd.DataFrame(df_drinks_con)
df.sort_values("COUNTRY")
country = df['COUNTRY'].head(10)
total_litres = df['TOTAL_LITRES'].head(10)

# Figure Size
fig = plt.figure(figsize=(10, 7))

# Horizontal Bar Plot

plt.title("Total litres consumed per person by country - 2010")
plt.xlabel("Country")
plt.ylabel("Total Litres of Alcohol")
plt.xticks(rotation='vertical')
plt.bar(country, total_litres)
plt.show()

#df_drinks_con.head(10).plot.bar(x="COUNTRY", y="TOTAL_LITRES", rot=70, title="Total litres consumed per by country - 2010");
p#lot.show();