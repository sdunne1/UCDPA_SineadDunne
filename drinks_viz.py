# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in merged dataframe csv file: df_drinks_con.csv
df_drinks_con = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\df_drinks_con.csv', sep=',', header=0,
                            index_col=0)
df_drinks_con.sort_values(["TOTAL_LITRES"], ascending=True)
print(df_drinks_con.head(5))

# Insight 1: Top 10 countries with the highest total litres consumed per person
total_by_country = df_drinks_con[['COUNTRY', 'TOTAL_LITRES']].groupby("COUNTRY").sum().sort_values(by='TOTAL_LITRES',
                                                                                          ascending=False).head(10)
total_by_country.plot(xlabel="COUNTRY", ylabel="TOTAL LITRES",
                                        kind="bar", title="Total Litres consumed per capita by Country (2010)", rot=45)
plt.show()

# Visualisation 1: Scatter plot chart to show sum of servings for each alcohol by continent for year 2010.
sns.load_dataset(df_drinks_con)



# df_drinks_con["TL_SUM"] = df_drinks_con.total_litres.sum()

# scatter_drinks = df_drinks_con.groupby(["CONTINENT"]).agg({'BEER': sum, 'WINE': sum, 'SPIRIT': sum})
sns.scatterplot(data=df_drinks_con,x='TOTAL_LITRES', y="BEER", hue="CONTINENT")
sns.scatterplot(data=df_drinks_con,x='TOTAL_LITRES', y="WINE", hue="CONTINENT")
sns.scatterplot(data=df_drinks_con,x='TOTAL_LITRES', y="SPIRIT", hue="CONTIENT")
plt.show()


