#Percentage of Total Sales by Borough
from requirements import *

sns.set(style="white")
colors = sns.color_palette("Blues_r")

percentage_sales = sales_df["BOROUGH"].value_counts()
explode=[0.1,0,0,0,0]
labels = ["Queens", "Brooklyn", "Manhattan", "Staten Island", "Bronx"]

# Draw a count plot to show the number of planets discovered each year
plt.pie(percentage_sales, colors=colors, explode=explode,
        autopct="%1.1f%%", shadow=True, startangle=140, labels=labels)

plt.title("Percentage of Total Sales by Borough (2017)")

plt.axis("equal")
plt.figure(figsize=(20,20))
plt.savefig("percenttotalsales.png")

plt.show()