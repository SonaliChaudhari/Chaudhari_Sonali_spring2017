
# coding: utf-8

# # QUESTION 2 PART 2

# In[1]:

#importing all the required lib

import string
import csv, sys
from pandas import Series, DataFrame
import pandas as pd


# In[30]:

df = pd.read_csv('Data/employee_compensation.csv')
p = df[df['Year Type']=='Calendar']
#p.head()


# In[37]:

s = p[['Job Family', 'Employee Identifier','Total Benefits','Total Compensation','Overtime', 'Salaries']]


# In[38]:

s.head()


# In[39]:

a = s.groupby(['Job Family','Employee Identifier']).mean().reset_index()


# In[86]:

a.head()


# In[87]:

a['Overtime_%']= (a['Overtime']/a['Salaries'])*100
#a.head()


# In[88]:

b = a[a['Overtime_%']> 5].reset_index()
#b.head


# In[89]:

c = b.groupby('Job Family')['Total Benefits','Total Compensation'].mean().reset_index()
#c.head()


# In[90]:

c['Total Benefit %']=( c['Total Benefits']/c['Total Compensation'])*100
#c.head()


# In[92]:

final = c.sort_values('Total Benefit %',ascending=False).reset_index()
#final


# In[93]:

final.head(5)


# In[94]:

with open('Q2_Part1.csv', 'a') as csvfile:
    final.to_csv(csvfile, header=True, index=False)

