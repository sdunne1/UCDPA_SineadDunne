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
total_by_country.plot(xlabel="Country", ylabel="Total Litres consumed per person",
                                                        kind="bar", title="Total litres consumed - top ten countries (2010)")
plt.show()

# Visualisation 1: Scatter plot chart to show sum of alcohol servings by continent.
scatter_drinks = df_drinks_con.groupby(["CONTINENT"]).agg({'BEER': sum, 'WINE': sum, 'SPIRIT': sum})

fig, ax = plt.subplots()
ax.plot(scatter_drinks['CONTINENT'], scatter_drinks['BEER'])

ax1 = scatter_drinks.plot(kind='scatter', x='WINE', y='CONTINENT', color='r')
ax2 = df.plot(kind='scatter', x='BEER', y='CONTINENT', color='b', ax=ax1)
ax3 = df.plot(kind='scatter', x='SPIRIT', y='CONTINENT', color='g', ax=ax1)

plt.show()



import numpy as np
import hvplot.pandas
import pandas as pd

df = pd.DataFrame(np.random.randn(100, 6), columns=['a', 'b', 'c', 'd', 'e', 'f'])

df.hvplot(x='a', y=['b', 'c', 'd', 'e'], kind='scatter')
