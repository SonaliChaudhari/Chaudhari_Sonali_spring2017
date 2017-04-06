
# coding: utf-8

# # QUESTION 4 PART 2

# In[1]:

#importing all the required lib

import string
import csv, sys
from pandas import Series, DataFrame
import pandas as pd


# In[4]:

# reading the csv file using pandas

df = pd.read_csv('Data/movies_awards.csv')

# displaying few rows of the dataframe using head()
df.head(2)


# In[19]:

df['Awards_Won'] = df['Awards'].str.extract('(\d+) win', expand=True)
#df.head()


# In[44]:

df['Awards_Nominated'] = df['Awards'].str.extract('(\d+) nomination', expand=True)
#df.head()


# In[ ]:

# GOLDENGLOBE AWARDS


# In[45]:

df['GoldenGlobe_Awards_Won']= df['Awards'].str.extract('Won (\d+) Golden Globe', expand=True)
#df.head()
df['GoldenGlobe_Awards_Nominated']= df['Awards'].str.extract('Nominated for (\d+) Golden Globe', expand=True)
#df.head()


# In[ ]:

# OSCAR AWARDS


# In[46]:

df['Oscar_Awards_Won']= df['Awards'].str.extract('Won (\d+) Oscar', expand=True)
#df.head()
df['Oscar_Awards_Nominated']= df['Awards'].str.extract('Nominated for (\d+) Oscar', expand=True)
#df.head()


# In[ ]:

# PRIME AWARDS


# In[21]:

df['Prime_Awards_Won']= df['Awards'].str.extract('Won (\d+) Primetime', expand=True)
#df.head()
df['Prime_Awards_Nominated']= df['Awards'].str.extract('Nominated for (\d+) Primetime', expand=True)
#df.head()


# In[22]:

# BAFTA AWARDS


# In[23]:

df['Bafta_Awards_Won']= df['Awards'].str.extract('Won (\d+) BAFTA', expand=True)
#df.head()
df['Bafta_Awards_Nominated']= df['Awards'].str.extract('Nominated for (\d+) BAFTA', expand=True)
#df.head()


# In[38]:

a = df[['Awards','Awards_Won','Awards_Nominated','GoldenGlobe_Awards_Won','GoldenGlobe_Awards_Nominated','Oscar_Awards_Won','Oscar_Awards_Nominated','Prime_Awards_Won','Prime_Awards_Nominated','Bafta_Awards_Won','Bafta_Awards_Nominated']]


# In[39]:

a.head()


# In[40]:

final  = a.fillna(0)


# In[41]:

final.head()


# In[48]:

# Storing the result in the csv

with open('Q4_Part1.csv', 'a') as csvfile:
    final.to_csv(csvfile, header=True)

