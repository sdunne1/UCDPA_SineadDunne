# importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read in merged dataframe csv file: df_drinks_con.csv
df_drinks_con = pd.read_csv(r'C:\Users\S_Dun\Desktop\UCDPA_SineadDunne\df_drinks_con.csv', sep=',', header=0,
                            index_col=0)
df_drinks_con.sort_values(["TOTAL_LITRES"], ascending=True)
print(df_drinks_con.head(4))

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

# Visualisation 3
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
    largest = row.index[maxFunction(row.iloc[1],row.iloc[2],row.iloc[3])]


    #if(row.iloc[1] >= row.iloc[2]) and (row.iloc[1] >= row.iloc[3]):
     #   largest = row.index[1]
    #elif(row.iloc[2] >= row.iloc[1]) and (row.iloc[2] >= row.iloc[3]):
     #   largest = row.index[2]
    #else:
     #   largest = row.index[3]
    #print(countryName, largest)
    #new_row = {'COUNTRY': countryName, 'PREF': largest}
    #print(new_row)
    df_drinks_con.loc[index,'PREF'] = largest

print(df_drinks_con.head(4))


print(df_pref_con)
# print(df_drinks_con.loc[row['BEER'] & row['WINE'] & row['SPIRIT']].max())

# df_conpref = [df_drinks_con["CONTINENT"]].iloc[:, 1:5]
# labels = 'Spirit','Beer', 'Total Litres','Wine'
# colors = ['#2ECC71','#2FF7F7','#F12BBE','#F4D03F']
# sections = [df_conpref.SPIRIT.sum(),
#            df_conpref.BEER.sum(),
#            df_conpref.TOTAL_LITRES.sum() ,
#            df_conpref.WINE.sum()]

plt.figure(figsize=(14, 8), dpi=75)
plt.pie(sections, labels=labels,wedgeprops=dict( alpha=1),
        startangle=90,
        #explode = (0,0,0,0),
        autopct = '%0.1f%%',
         textprops={
                'fontsize': 10,
                'fontweight': 'normal'}
            )



