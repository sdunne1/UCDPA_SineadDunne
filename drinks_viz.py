# importing libraries
import pandas as pd
import matplotlib.pyplot as plt


# Read in merged dataframe csv file: df_drinks_con.csv
df_drinks_con = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\df_drinks_con.csv', sep=',', header=0)
df_drinks_con.sort_values(["TOTAL_LITRES"], ascending=True)
print(df_drinks_con)

# Insight 1: Top 10 countries with the highest total litres consumed per person
total_by_country = df_drinks_con[['COUNTRY','TOTAL_LITRES']].groupby("COUNTRY").sum().sort_values(by='TOTAL_LITRES', ascending=False).head(10)
total_by_country.plot(xlabel="Country", ylabel="Total Litres consumed",
                                                            kind="bar", title="Total litres consumed per by country")
plt.show()
