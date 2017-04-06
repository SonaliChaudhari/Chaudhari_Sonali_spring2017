
# coding: utf-8

# # Question 2 Part 1

# In[1]:

import string
import csv, sys
from pandas import Series, DataFrame
import pandas as pd


# In[2]:

df = pd.read_csv('Data/employee_compensation.csv')

s = pd.DataFrame(df[['Organization Group','Department','Total Compensation']])

s['Total'] = s.groupby(['Department', 'Organization Group'])['Total Compensation'].transform('sum')


# In[3]:

s = s.drop_duplicates(subset=['Department', 'Organization Group']) #, keep=False)


# In[4]:

p = s[['Organization Group','Department','Total']]


# In[5]:

p.head(10)


# In[7]:

with open('Q2_Part1.csv', 'a') as csvfile:
    p.to_csv(csvfile, header=True)

