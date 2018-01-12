#Dependencies
import pandas as pd 
from matplotlib import pyplot as plt
import numpy as np 
import seaborn as sns 
import requests as req
import random 

def CreateDataframe():
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

    #Create Price Bins and Dataframe for later
    price_bins = [0, 250000, 500000, 750000, 1000000, 1500000, 2000000, 3000000, 4000000, 1000000000]

    # Create the names for the bins
    bin_names = ['$0-250K', '$250K-$500K', '$500K-$750K', '$750K-$1M', '$1M-$1.5M', '$1.5M-$2M',
                '$2M-$3M', '$3M-$4M', '4000000+']

    sales_df["Price Category"] = pd.cut(sales_df[' SALE PRICE '], price_bins, labels=bin_names)

    return sales_df
