#Price Compared with Year Built(Sample Taken)
from requirements import *

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
lgnd = plt.legend(loc='best')
lgnd.legendHandles[0]._sizes = [100]
lgnd.legendHandles[1]._sizes = [100]
lgnd.legendHandles[2]._sizes = [100]
lgnd.legendHandles[3]._sizes = [100]
lgnd.legendHandles[4]._sizes = [100]

plt.title("Price Compared with Year Built (2017)")

plt.savefig("pricevyear.png")

plt.show()

