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

#Sales Per Borough
from requirements import *

sns.set(style="dark")
colors = sns.color_palette("Blues_r")

# Draw a count plot to show the number of sales per borough
g = sns.factorplot(x="BOROUGH", data=sales_df, kind="count",
                   palette=colors, size=6, aspect=1.5, order=['1','2','13'])
g.set_xticklabels(step=1)
plt.grid(color="white") 
plt.title("Sales Per Borough (2017)")
plt.savefig("totalsales.png")


plt.show()
