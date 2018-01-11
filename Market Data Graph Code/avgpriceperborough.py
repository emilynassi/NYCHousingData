#Average Price Per Borough
#Dependencies
import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np 
import seaborn as sns 
import requests as req
import random 
from requirements import CreateDataframe 
dataframe = CreateDataframe()

dataframe.head()

sns.set_style("dark")

average_price = sales_df.groupby(["BOROUGH"])[" SALE PRICE "].mean()

avg_price_df = pd.DataFrame(average_price)
x = avg_price_df.index
y = average_price
plt.figure(figsize=(10,6))

plt.plot(x, y, color="#3182bd")
plt.title("Average Price Per Borough (2017)")

plt.grid(color="white") 
plt.savefig("avgprice.png")

plt.show()
