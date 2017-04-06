
# coding: utf-8

# # QUESTION 2 PART 2

# In[1]:

#importing all the required lib

import string
import csv, sys
from pandas import Series, DataFrame
import pandas as pd


# In[30]:

# reading the csv file using pandas
df = pd.read_csv('Data/employee_compensation.csv')

# Retrieving the entries for the Calendar year Type
p = df[df['Year Type']=='Calendar']
#p.head()


# In[37]:

# Retrieving only the required columns
s = p[['Job Family', 'Employee Identifier','Total Benefits','Total Compensation','Overtime', 'Salaries']]


# In[1]:

#s.head()


# In[39]:

# Grouping the entries by Job Family and taking the mean
a = s.groupby(['Job Family','Employee Identifier']).mean().reset_index()


# In[2]:

#a.head()


# In[87]:

# calculating the overtime percentage

a['Overtime_%']= (a['Overtime']/a['Salaries'])*100
#a.head()


# In[88]:

# Retrieving the required rows that families having overtime percentage more than 5
b = a[a['Overtime_%']> 5].reset_index()
#b.head


# In[89]:

# Finding the average Total Benefits, average Total Compensation for every family
c = b.groupby('Job Family')['Total Benefits','Total Compensation'].mean().reset_index()
#c.head()


# In[90]:

# calculating the Total Benefit percentage
c['Total Benefit %']=( c['Total Benefits']/c['Total Compensation'])*100
#c.head()


# In[92]:

#Sorting the dataframe in descending order of Total Benefits %

final = c.sort_values('Total Benefit %',ascending=False).reset_index()
#final


# In[93]:

# Displaying the final output using head()
final.head(5)


# In[95]:

# Storing the result in the csv

with open('Q2_Part2.csv', 'a') as csvfile:
    final.to_csv(csvfile, header=True, index=False)

