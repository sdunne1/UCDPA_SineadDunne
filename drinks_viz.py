# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in merged dataframe csv file: df_drinks_con.csv
df_drinks_con = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\df_drinks_con.csv', sep=',', header=0,
                            index_col=0)
df_drinks_con.sort_values(["TOTAL_LITRES"], ascending=True)

# Visualisation 1: Top 10 countries with the highest total litres consumed per person
total_by_country = df_drinks_con[['COUNTRY', 'TOTAL_LITRES']].groupby("COUNTRY").sum().sort_values(by='TOTAL_LITRES',
                                                                                          ascending=False).head(10)
total_by_country.plot(xlabel="COUNTRY", ylabel="TOTAL LITRES",
                                        kind="bar", title="Total Litres consumed per capita by Country (2010)", rot=12)
plt.show()

# Visualisation 2A: Top 10 countries for wine consumers
wine = df_drinks_con[['COUNTRY', 'WINE']].groupby("COUNTRY").sum().sort_values(by="WINE", ascending=False).head(10)
ax = sns.barplot(x="WINE", y="COUNTRY", data=wine)
ax.set(ylabel='COUNTRY', xlabel='WINE SERVINGS')
ax.set_title("Top 10 Global Wine Consumers")

# Visualisation 2B: Top 10 countries for spirit consumers
spirits = df_drinks_con.groupby("COUNTRY")["SPIRIT"].max().reset_index().sort_values(by='SPIRIT',ascending=False)[:10]
ax = sns.barplot(x="SPIRIT", y="COUNTRY", data=spirits)
ax.set(ylabel='COUNTRY', xlabel='SPIRIT SERVINGS')
ax.set_title("Top 10 Global Spirits Consumers")

# Visualisation 2C: Top 10 countries for beer consumers
beer = df_drinks_con.groupby("COUNTRY")["BEER"].max().reset_index().sort_values(by='BEER',ascending=False)[:10]
ax = sns.barplot(x="BEER", y="COUNTRY", data=beer)
ax.set(ylabel='COUNTRY', xlabel='BEER SERVINGS')
ax.set_title("Top 10 Global Beer Consumers")

# Visualisation 3 Alcohol preference by continent: Setting up
# Create new column in dataframe.
# # Create function that gets max value of columns BEER, SPIRIT, WINE & RETURN COLUMN HEADER TO PREF.
df_drinks_con['PREF'] = ""

def maxFunction(value1, value2, value3):
    if (value1 >= value2) and (value1 >= value3):
        return 1
    elif (value2 >= value1) and (value2 >= value3):
        return 2
    else:
        return 3

for index, row in df_drinks_con.iterrows():
    countryName = row.iloc[0]
    largest = row.index[maxFunction(row.iloc[1], row.iloc[2], row.iloc[3])]
    df_drinks_con.loc[index,'PREF'] = largest
    print(df_drinks_con.columns)

# Visualisation 3: Alcohol pref by continent Pie Chart
pref_results = df_drinks_con.groupby("CONTINENT")["PREF"].value_counts()

y = ["SPIRIT", "BEER", "BEER", "SPIRIT", "BEER", "BEER"]
mylabels = ["Asia", "Africa", "Europe", "North America", "South America", "Oceania"]
myexplode = [0.0, 0.2, 0, 0, 0, 0]
colours = ['tab:blue', 'tab:cyan', 'tab:gray', 'tab:orange', 'tab:red', 'tab:yellow']

fig, ax = plt.subplots()
ax.pie(y, labels=mylabels, colors=colours, explode=myexplode, shadow=True, autopct='%.0f%%')
ax.set_title("Preferred option by Continent")
plt.show()