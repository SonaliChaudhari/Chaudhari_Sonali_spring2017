
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

df = pd.read_csv('Data/cricket_matches.csv')


# In[6]:

a=df[['home','winner','innings1','innings1_runs','innings2','innings2_runs']]


# In[7]:

a.head()


# In[9]:

a['HOME'] = np.where(a['home']==a['winner'],'1','0')
#a.head()


# In[10]:

b = a[a['HOME']=='1']
#b


# In[11]:

b['SCORE'] = np.where(b['home']==b['innings1'], b['innings1_runs'], b['innings2_runs'])


# In[12]:

#b.head()


# In[13]:

c = b[['home','SCORE']]
c['SCORE'] = c.groupby(['home'])['SCORE'].transform('mean')


# In[14]:

c.head()


# In[75]:

with open('Q3_Part1.csv', 'a') as csvfile:
    c.to_csv(csvfile, header=True)

