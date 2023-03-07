# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:14:51 2023

@author: saiteja
"""

import pandas as pd;
df = pd.read_csv('transaction.csv', sep=';')
df.info()
df.isnull()
CostPerItem = df['CostPerItem']
NumberOfItemsPurchased = df['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem*NumberOfItemsPurchased

#adding a New Column for the DataFrame
df['CostPerTransaction'] = df['CostPerItem'] * df['NumberOfItemsPurchased']
#Sales per transaction
df['SalesPerTransaction'] = df['SellingPricePerItem'] * df['NumberOfItemsPurchased']

# Calculating Profit

df['Profit'] = df['SalesPerTransaction'] - df['CostPerTransaction']

df['Markup'] = (df['SalesPerTransaction'] - df['CostPerTransaction'])/df['CostPerTransaction']

#Round Markup

RoundMarkup = round(df['Markup'], 2)

df['Markup'] = RoundMarkup

# Converting the DataTypes

Day = df['Day'].astype(str)
Year = df['Year'].astype(str)
My_Date = df['Month']+'-'+Day+'-'+Year

#Combining My_Date with the Table
df['Date'] = My_Date

#Using Split to split the Client_Keywords
#New_Var = column.str.split('sep', expand = True)
Split_Col = df['ClientKeywords'].str.split(',', expand = True);

#Creating New Columns in DataFrame from the split column

df['ClientAge'] = Split_Col[0]
df['ClientType'] = Split_Col[1]
df['ContractLength'] = Split_Col[2]

#Using the Replace Function

df['ClientAge'] = df['ClientAge'].str.replace('[','')
df['ContractLength'] = df['ContractLength'].str.replace(']','')

#Using the Lower Case to change the itemDescription to Lower Case

df['ItemDescription'] = df['ItemDescription'].str.lower()

#Bringing in a New Dataset to merge with the current DataSet

df1 = pd.read_csv('value_inc_seasons.csv', sep = ';')

df = pd.merge(df,df1, on = 'Month')

#Dropping Columns

df = df.drop(['ClientKeywords','Day','Month','Year'],axis = 1)
df.info()

#Export the dataset to CSV

df.to_csv('ValueInc_Cleaned.csv', index = False)


