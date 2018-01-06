#Dependencies
import pandas as pd 
import matplotlib as plt
import numpy as np 
import seaborn as sns 
import requests as req

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
sales_df.dropna(axis=0, how='any', thresh=3, subset=None, inplace=False)

sales_df["BOROUGH"].astype(str).replace("1.0", "Manhattan")
