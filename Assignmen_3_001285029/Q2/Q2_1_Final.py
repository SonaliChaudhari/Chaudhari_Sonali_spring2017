
# coding: utf-8

# # Question 2 Part 1

# In[1]:

#importing all the required lib

import string
import csv, sys
from pandas import Series, DataFrame
import pandas as pd


# In[2]:

# reading the csv file using pandas
df = pd.read_csv('Data/employee_compensation.csv')

# Retrieving only the required columns
s = pd.DataFrame(df[['Organization Group','Department','Total Compensation']])

# Grouping the entries by Department and summing the total compensation for a particular department
s['Total'] = s.groupby(['Department', 'Organization Group'])['Total Compensation'].transform('sum')


# In[3]:

# Eliminating duplicate columns
s = s.drop_duplicates(subset=['Department', 'Organization Group']) #, keep=False)


# In[4]:

## Retrieving only the required columns
p = s[['Organization Group','Department','Total']]


# In[5]:

# Displaying the final output using head()

p.head(10)


# In[7]:

# Storing the result in the csv

with open('Q2_Part1.csv', 'a') as csvfile:
    p.to_csv(csvfile, header=True)

