from requirements import *

#Create Sales by Month Dataframe
'''sales_df['SALE DATE']= pd.to_datetime(sales_df['SALE DATE'])
heatmap_df = pd.concat([sales_df['BOROUGH'], sales_df['SALE DATE']], axis=1)#heatmap_df["SALE MONTH"] = heatmap_df['SALE DATE'].dt.strftime('%B')

monthly_sales = heatmap_df.groupby(["SALE MONTH"])['BOROUGH'].value_counts()
monthly_sales = pd.DataFrame(monthly_sales)'''

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
                          
