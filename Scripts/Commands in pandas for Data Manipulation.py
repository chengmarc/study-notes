# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 20:59:25 2022

@author: Admin
"""
import os
import pandas as pd
import numpy as np
from pandasql import sqldf

from sys import path
parent_folder = r'C:\Users\Admin\Desktop'
if parent_folder not in path: path.append(parent_folder)

os.path.join('Path A', 'Path B')  #Joining path

# %% Oracle Connection
import cx_Oracle
ip = 'xxx.bns'
port = 0000
service_name= 'xxx.bns'
user = 'user'
pw = 'password'
dsn = cx_Oracle.makedsn(ip, port, service_name = service_name)

# %% Read and Write
df = pd.read_csv('Path', usecol=['List of Columns'])
df = pd.read_parquet('Path', columns=['List of Columns'])
df.to_csv()                     
df.to_parquet()

df = pd.concat([df1, df2], ignore_index = True) # Concat

# %% Filtering and Conditioning
df = df['Boolean Value']
df = df[df['Column Name'] < 0]
df = df[df['Column Name'] == 'Value']

# %% Manipulating Data
df['Column Name'] = df['Column Name'].str[:3]
df['Column Name'] = pd.DatetimeIndex(df['Column Name'])

df = df.replace(0, np.nan)
df.notnull().sum()

# %% Iterations in DataFrames
for row, rows in df.iterrows():         #iterate rows
    for col in df.columns:              #iterate columns
        value = df.loc[row, col]        #get value based on location
        df.at[row, col] = 'value'       #assigning value based on location

# %% Executing Query in Python
pysql = lambda query: sqldf(query, globals())
query = 'SELECT * FROM df'
df = pysql(query)                               