
# coding: utf-8

# # QUESTION 1 PART 1

# In[2]:

# importing all the necessary lib
import csv, sys
from pandas import Series, DataFrame
import pandas as pd
import calendar
import datetime as dt


# In[3]:

#3178 18101


# In[4]:

df = pd.read_csv('Data/vehicle_collisions.csv')


# In[5]:

df['DATE'] =  pd.to_datetime(df['DATE'])


# In[6]:

df['YEAR'], df['MONTH'] = df['DATE'].apply(lambda x: x.year), df['DATE'].apply(lambda x: x.month)


# In[11]:

p = df[(df['YEAR']==2016)]


# In[13]:

NYC_Frame = p.groupby('MONTH')['UNIQUE KEY'].count().reset_index()


# In[14]:

Total_Frame = NYC_Frame[['MONTH','UNIQUE KEY']]


# In[34]:

#Total_Frame.head()


# In[16]:

Part_Frame = p[(p['BOROUGH'] == 'MANHATTAN')]


# In[18]:

MANHATTAN_Frame = Part_Frame.groupby('MONTH')['UNIQUE KEY'].count().reset_index()


# In[19]:

MANHATTAN_Frame = MANHATTAN_Frame[['MONTH','UNIQUE KEY']]


# In[35]:

#MANHATTAN_Frame.head()


# In[21]:

result_frame = Total_Frame.merge(MANHATTAN_Frame,on='MONTH')


# In[24]:

result_frame.columns = ['MONTH','NYC','MANHATTAN']


# In[26]:

result_frame.head()


# In[33]:

result_frame['Percent'] = (result_frame['MANHATTAN']/result_frame['NYC'])*100


# In[28]:

result_frame.head()


# In[30]:

result_frame['MONTH'] = result_frame['MONTH'].apply(lambda x: calendar.month_abbr[x])


# In[31]:

result_frame.head()


# In[ ]:

with open('Q1_Part1.csv', 'a') as csvfile:
    p.to_csv(csvfile, header=True)

