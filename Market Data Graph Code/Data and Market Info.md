
# NYC Housing Data and Market Report

# Clean and Sort Data


```python
# Dependencies
import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np 
import seaborn as sns 
import requests as req
import random 

#Read CSVs and Combine to One Dataframe
file_one = "rollingsales_bronx.csv"
file_two = "rollingsales_brooklyn.csv"
file_three = "rollingsales_manhattan.csv"
file_four = "rollingsales_queens.csv"
file_five = "rollingsales_statenisland.csv"

bronx_pd = pd.read_csv(file_one)
brooklyn_pd = pd.read_csv(file_two)
manhattan_pd = pd.read_csv(file_three)
queens_pd = pd.read_csv(file_four)
staten_island_pd = pd.read_csv(file_five)
sales_df = pd.concat([manhattan_pd, bronx_pd, brooklyn_pd, queens_pd, staten_island_pd])

#Clean missing rows, change Borough numbers to names and sort out residential buildings
sales_df['BOROUGH'] = sales_df['BOROUGH'].map({1:'Manhattan', 2:'Bronx', 3:'Brooklyn', 4:'Queens', 5:'Staten Island'})
sales_df['BUILDING CLASS'], sales_df['CATEGORY'] = sales_df['BUILDING CLASS CATEGORY'].str.split(' ', 1).str
del (sales_df['BUILDING CLASS CATEGORY'], sales_df['BLOCK'], sales_df['LOT'],  sales_df['EASE-MENT'],  sales_df['TAX CLASS AT PRESENT'],
     sales_df['TAX CLASS AT TIME OF SALE'])
sales_df = sales_df.replace('-', np.nan).dropna(thresh=7)
sales_df = sales_df[~sales_df['BUILDING CLASS'].isin(['11A'])]
sales_df[['BUILDING CLASS']] = sales_df[['BUILDING CLASS']].apply(pd.to_numeric)
sales_df[' SALE PRICE '] = pd.to_numeric(sales_df[' SALE PRICE ']) 
#Use Loop to sort out residential buildings

# Create a list to store the data
sale_type = []

# For each row in the column,
for row in sales_df['BUILDING CLASS']:
    if row < 4 :
        sale_type.append('Residential Sale')
    elif row == 6:
        sale_type.append('Residential Sale')
    elif row == 9:
        sale_type.append('Residential Sale')
    elif row == 10:
        sale_type.append('Residential Sale')
    elif row == 12:
        sale_type.append('Residential Sale')
    elif row == 13:
        sale_type.append('Residential Sale')
    elif row == 15:
        sale_type.append('Residential Sale')
    elif row == 16:
        sale_type.append('Residential Sale')
    elif row == 17:
        sale_type.append('Residential Sale')
    else:
        # Append Other
        sale_type.append('Other')
        
# Create a column from the list
sales_df['sale_type'] = sale_type

sales_df = sales_df[~sales_df['sale_type'].isin(['Other'])]

sales_df.max()
```

# Sales Per Borough


```python
sns.set(style="dark")
colors = sns.color_palette("Blues_r")

# Draw a count plot to show the number of sales per borough
g = sns.factorplot(x="BOROUGH", data=sales_df, kind="count",
                   palette=colors, size=6, aspect=1.5)
g.set_xticklabels(step=1)
plt.grid(color="white") 
plt.title("Sales Per Borough (2017)")
plt.savefig("totalsales.png")


plt.show()
```


![png](output_4_0.png)


# Average Price Per Borough


```python
#Average Price Per Borough
sns.set_style("dark")

average_price = sales_df.groupby(["BOROUGH"])[" SALE PRICE "].mean()

avg_price_df = pd.DataFrame(average_price)
x = avg_price_df.index
y = average_price
plt.figure(figsize=(10,6))

plt.plot(x, y, color="#3182bd")
plt.title("Average Price Per Borough (2017)")
plt.xlabel("Borough")
plt.ylabel("Price ($)")

plt.grid(color="white") 
plt.savefig("avgprice.png")

plt.show()

```


![png](output_6_0.png)


# Percentage of Total Sales by Borough


```python
# Percentage of Total Sales by Borough
sns.set(style="white")
colors = sns.color_palette("Blues_r")

percentage_sales = sales_df["BOROUGH"].value_counts()
explode=[0.1,0,0,0,0]
labels = ["Queens", "Brooklyn", "Manhattan", "Staten Island", "Bronx"]

# Draw a count plot to show the number of planets discovered each year
plt.pie(percentage_sales, colors=colors, explode=explode,
        autopct="%1.1f%%", shadow=True, startangle=140, labels=labels)

plt.title("Percentage of Total Sales by Borough (2017)")

plt.# Percentage of Total Sales by Boroughaxis("equal")

fig = plt.gcf()
fig.set_size_inches(10,10)

plt.savefig("percenttotalsales.png")

plt.show()
```


![png](output_8_0.png)


# Price Compared with Year Built


```python
#Price Compared with Year Built(Sample Taken in order to show trends)
filtered_df = sales_df.replace('-', np.nan).dropna(how='any')
filtered_df = filtered_df.sample(n=1500, replace=True)
manhattan = filtered_df[filtered_df['BOROUGH'] == 'Manhattan']
brooklyn = filtered_df[filtered_df['BOROUGH'] == 'Brooklyn']
bronx = filtered_df[filtered_df['BOROUGH'] == 'Bronx']
staten = filtered_df[filtered_df['BOROUGH'] == 'Staten Island']
queens = filtered_df[filtered_df['BOROUGH'] == 'Queens']

#add grid
sns.set_style("dark")
plt.grid(color="white") 

plt.scatter(manhattan['YEAR BUILT'], manhattan[' SALE PRICE '], color="#eff3ff", s=20, edgecolor = 'black',
        label = 'Manhattan', alpha = .75)
plt.scatter(bronx['YEAR BUILT'], bronx[' SALE PRICE '], color="#bdd7e7", edgecolor = 'black',
        label = 'Bronx', alpha = .75)
plt.scatter(brooklyn['YEAR BUILT'], brooklyn[' SALE PRICE '], color="#6baed6", edgecolor = 'black',
        label = 'Brooklyn', alpha = .75)
plt.scatter(queens['YEAR BUILT'], queens[' SALE PRICE '], color="#3182bd", edgecolor = 'black',
        label = 'Queens', alpha = .75)
plt.scatter(staten['YEAR BUILT'], staten[' SALE PRICE '], color="#08519c", edgecolor = 'black',
        label = 'Staten Island', alpha = .75)

#change field size
plt.xlim(1900, 2025)
plt.ylim(250000,2000000)

#add legend
lgnd = plt.legend(loc='upper right')
lgnd.legendHandles[0]._sizes = [100]
lgnd.legendHandles[1]._sizes = [100]
lgnd.legendHandles[2]._sizes = [100]
lgnd.legendHandles[3]._sizes = [100]
lgnd.legendHandles[4]._sizes = [100]

plt.title("Price Compared with Year Built (2017)")
plt.xlabel("Borough")
plt.ylabel("Price ($)")

fig = plt.gcf()
fig.set_size_inches(12,10)
plt.savefig("pricevyear.png")

plt.show()


```


![png](output_10_0.png)



```python
#Create Sales by Month Dataframe
'''sales_df['SALE DATE']= pd.to_datetime(sales_df['SALE DATE'])
heatmap_df = pd.concat([sales_df['BOROUGH'], sales_df['SALE DATE']], axis=1)#heatmap_df["SALE MONTH"] = heatmap_df['SALE DATE'].dt.strftime('%B')

monthly_sales = heatmap_df.groupby(["SALE MONTH"])['BOROUGH'].value_counts()
monthly_sales = pd.DataFrame(monthly_sales)'''

```




    'sales_df[\'SALE DATE\']= pd.to_datetime(sales_df[\'SALE DATE\'])\nheatmap_df = pd.concat([sales_df[\'BOROUGH\'], sales_df[\'SALE DATE\']], axis=1)#heatmap_df["SALE MONTH"] = heatmap_df[\'SALE DATE\'].dt.strftime(\'%B\')\n\nmonthly_sales = heatmap_df.groupby(["SALE MONTH"])[\'BOROUGH\'].value_counts()\nmonthly_sales = pd.DataFrame(monthly_sales)'



# Sales by Month Heatmap



```python
#Sales by Month Heatmap
sns.set()

monthly_sales = pd.read_csv('monthlysales.csv')
sales = monthly_sales.pivot("SALE MONTH", "BOROUGH", "COUNT")
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
borough = ['Bronx', 'Staten Island','Manhattan', 'Brooklyn', 'Queens']
sales = sales.reindex(months,borough)
#borough = sales.reindex(borough)

#Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9,7))
sns.heatmap(sales, annot=True, fmt="d", linewidths=.5, ax=ax, cmap="Blues")

plt.title("Sales by Month per Borough (2017)")

plt.savefig("monthlysales.png")

plt.show()
                          

```


![png](output_13_0.png)

