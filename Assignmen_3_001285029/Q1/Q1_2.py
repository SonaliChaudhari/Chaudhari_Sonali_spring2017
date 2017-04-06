
# coding: utf-8

# ## QUESTION 1 PART 2

# In[1]:

#importing all the required lib

import string
import csv, sys
from pandas import Series, DataFrame
import pandas as pd


# In[2]:

# reading the csv file using pandas

df = pd.read_csv('Data/vehicle_collisions.csv')


# In[3]:

# displaying few rows of the dataframe using head()

#df.head(3)


# In[4]:

# Retrieving only the required columns

a = df[['UNIQUE KEY','BOROUGH','VEHICLE 1 TYPE','VEHICLE 2 TYPE','VEHICLE 3 TYPE','VEHICLE 4 TYPE','VEHICLE 5 TYPE']]
b  = a.fillna(0)
#b.head(3)


# In[5]:

# Finding the count where 5 vehicles were involved in collision    


# In[6]:

v5 = b[b['VEHICLE 5 TYPE']!= 0]
v5 = v5.groupby('BOROUGH')['UNIQUE KEY'].count().reset_index()
v5


# In[7]:

# Finding the count where 4 vehicles were involved in collision    


# In[8]:

v4 = b[(b['VEHICLE 5 TYPE']== 0) & (b['VEHICLE 4 TYPE']!= 0)]
v4 = v4.groupby('BOROUGH')['UNIQUE KEY'].count().reset_index()
v4


# In[9]:

# Combining the dataframes for 4 or 5 vehicles involved collisons


# In[10]:

m = v5.merge(v4, on = 'BOROUGH')
m['MORE_VEHICLES_INVOLVED'] = m['UNIQUE KEY_x']+m['UNIQUE KEY_y']
M= m[['BOROUGH','MORE_VEHICLES_INVOLVED']]
M


# In[11]:

# Finding the count where 3 vehicles were involved in collision    


# In[12]:

v3 = b[(b['VEHICLE 5 TYPE']== 0) & (b['VEHICLE 4 TYPE']== 0) & (b['VEHICLE 3 TYPE']!= 0)]
v3 = v3.groupby('BOROUGH')['UNIQUE KEY'].count().reset_index()
v3


# In[13]:

# Finding the count where 2 vehicles were involved in collision    


# In[14]:

v2 = b[(b['VEHICLE 5 TYPE']== 0) & (b['VEHICLE 4 TYPE']== 0) & (b['VEHICLE 3 TYPE']== 0) & (b['VEHICLE 2 TYPE']!= 0)]
v2 = v2.groupby('BOROUGH')['UNIQUE KEY'].count().reset_index()
v2


# In[15]:

# Finding the count where 1 vehicles were involved in collision    


# In[16]:

v1 = b[(b['VEHICLE 5 TYPE']== 0) & (b['VEHICLE 4 TYPE']== 0) & (b['VEHICLE 3 TYPE']== 0) & (b['VEHICLE 2 TYPE']== 0) & (b['VEHICLE 1 TYPE']!= 0)]
v1 = v1.groupby('BOROUGH')['UNIQUE KEY'].count().reset_index()
v1


# In[17]:

# Merging all the dataframes(v1,v2,v3,M)
final = v1.merge(v2, on = 'BOROUGH').merge(v3, on = 'BOROUGH').merge(M, on = 'BOROUGH')

# Renaming the columns of the dataframe
final.columns =['BOROUGH','ONE_VEHICLES_INVOLVED','TWO_VEHICLES_INVOLVED','THREE_VEHICLES_INVOLVED','MORE_VEHICLES_INVOLVED']


# In[18]:

final= final[final['BOROUGH']!=0]

# Displaying the final output using head()
final.head()


# In[19]:

# Storing the result in the csv

with open('Q1_Part2.csv', 'a') as csvfile:
    final.to_csv(csvfile, header=True)

