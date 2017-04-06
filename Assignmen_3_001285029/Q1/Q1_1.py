
# coding: utf-8

# # QUESTION 1 PART 1

# In[2]:

# importing all the necessary lib

import csv, sys
from pandas import Series, DataFrame
import pandas as pd
import calendar
import datetime as dt


# In[4]:

# reading the csv file using pandas

df = pd.read_csv('Data/vehicle_collisions.csv')


# In[6]:

# Converting the date in string into datetime format
df['DATE'] =  pd.to_datetime(df['DATE'])

# Separating the month and year part of the date column
df['YEAR'], df['MONTH'] = df['DATE'].apply(lambda x: x.year), df['DATE'].apply(lambda x: x.month)

# Retrieving the entries for the 2016 year only
p = df[(df['YEAR']==2016)]


# In[13]:

# Count of all the entries for collisions grouped by Month
NYC_Frame = p.groupby('MONTH')['UNIQUE KEY'].count().reset_index()

# Finding total collisons per month
Total_Frame = NYC_Frame[['MONTH','UNIQUE KEY']]


# In[34]:

#Total_Frame.head()


# In[16]:

# Retrieving the entries 'MANHATTAN' only
Part_Frame = p[(p['BOROUGH'] == 'MANHATTAN')]


# In[18]:

# Count of all the entries for collisions grouped by Month that happend in 'MANHATTAN' only
MANHATTAN_Frame = Part_Frame.groupby('MONTH')['UNIQUE KEY'].count().reset_index()

# Finding total collisons per month that happend in 'MANHATTAN' only
MANHATTAN_Frame = MANHATTAN_Frame[['MONTH','UNIQUE KEY']]


# In[35]:

#MANHATTAN_Frame.head()


# In[21]:

# Merging the two dataframes on their common 'MONTH' column

result_frame = Total_Frame.merge(MANHATTAN_Frame,on='MONTH')


# In[24]:

# Renaming the columns of the dataframe
result_frame.columns = ['MONTH','NYC','MANHATTAN']


# In[26]:

# Displaying the output using head()
result_frame.head()


# In[33]:

# Adding new column, calculating and storing  the percentage of collision in MANHATTAN to total collisions by month
result_frame['Percent'] = (result_frame['MANHATTAN']/result_frame['NYC'])*100


# In[28]:

# Displaying the output using head()
result_frame.head()


# In[30]:

# Mapping the month number to get month name using lambda function

result_frame['MONTH'] = result_frame['MONTH'].apply(lambda x: calendar.month_abbr[x])


# In[31]:

# Displaying the final output using head()
result_frame.head()


# In[ ]:

# Storing the result in the csv

with open('Q1_Part1.csv', 'a') as csvfile:
    p.to_csv(csvfile, header=True)

