# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read in merged dataframe csv file: df_drinks_con.csv
df_drinks_con = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\df_drinks_con.csv', sep=',', header=0,
                            index_col=0)
df_drinks_con.sort_values(["TOTAL_LITRES"], ascending=True)
print(df_drinks_con)

# Insight 1: Top 10 countries with the highest total litres consumed per person
total_by_country = df_drinks_con[['COUNTRY', 'TOTAL_LITRES']].groupby("COUNTRY").sum().sort_values(by='TOTAL_LITRES',
                                                                                          ascending=False).head(10)
total_by_country.plot(xlabel="Country", ylabel="Total Litres consumed",
                                                        kind="bar", title="Total litres consumed - top ten countries")
plt.show()

# Visualisation 1:
sns.load_dataset(df_drinks_con)
df_drinks_con.head()

# df_drinks_con.loc[:, ["CONTINENT", "COUNTRY", "BEER", "WINE", "SPIRIT"]]

scatter_drinks = df_drinks_con.groupby(["CONTINENT"]).agg({'BEER': sum, 'WINE': sum, 'SPIRIT': sum})
print(scatter_drinks)

sns.relplot(x='CONTINENT', y='BEER', data=scatter_drinks)
plt.show()


