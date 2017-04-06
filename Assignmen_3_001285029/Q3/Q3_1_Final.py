
# coding: utf-8

# # QUESTION 3 PART 1

# In[4]:

# importing all the necessary lib

import csv, sys
from pandas import Series, DataFrame
import numpy as np
import pandas as pd
import calendar
import datetime as dt


# In[5]:

# reading the csv file using pandas

df = pd.read_csv('Data/cricket_matches.csv')


# In[6]:

# Retrieving only the required columns
a=df[['home','winner','innings1','innings1_runs','innings2','innings2_runs']]


# In[7]:

a.head()


# In[9]:

# Assigning '1' to the column 'HOME' if host is the winner else '0'
a['HOME'] = np.where(a['home']==a['winner'],'1','0')
#a.head()


# In[10]:

# Considering only the cases where the host is the winner
b = a[a['HOME']=='1']
#b


# In[11]:

# Checking which inning the host played and taking the scores of it.
b['SCORE'] = np.where(b['home']==b['innings1'], b['innings1_runs'], b['innings2_runs'])


# In[12]:

#b.head()


# In[13]:

# Retrieving only the required columns
c = b[['home','SCORE']]

# Grouping the data by Home and Taking the average of the scores for each home
c['SCORE'] = c.groupby(['home'])['SCORE'].transform('mean')


# In[14]:

## Displaying the final output using head()
c.head()


# In[75]:

# Storing the result in the csv
with open('Q3_Part1.csv', 'a') as csvfile:
    c.to_csv(csvfile, header=True)

