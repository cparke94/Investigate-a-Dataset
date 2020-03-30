#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("h:/downloads/noshowappointments-kagglev2-may-2016.csv")


# In[3]:


df.describe()


# In[4]:


df.rename(columns = {'Handcap': 'Handicap'}, inplace = True)


# In[6]:


Exploratory_Analysis = ['Gender','Hipertension','Alcoholism','Diabetes']
for r in Exploratory_Analysis :
    print(df.groupby(r)['No-show'].mean())


# In[7]:


Exploratory_Analysis = ['Gender','Hipertension','Alcoholism','Diabetes']
for r in Exploratory_Analysis :
    print(df.groupby(r)['No-show'].mean())


# In[8]:


df.columns


# In[9]:


df['No-show'].replace("No", 0,inplace=True)
df['No-show'].replace("Yes", 1,inplace=True)


# In[10]:


Exploratory_Analysis = ['Gender','Hipertension','Alcoholism','Diabetes']
for r in Exploratory_Analysis :
    print(df.groupby(r)['No-show'].mean())


# In[11]:


df['Handicap'] = pd.Categorical(df['Handicap'])
#Convert to Dummy Variables
Handicap = pd.get_dummies(df['Handicap'], prefix = 'Handicap')
df = pd.concat([df, Handicap], axis=1)


# In[12]:


handicaps = ["Handicap_1", "Handicap_2", "Handicap_3", "Handicap_4"]
for h in handicaps:
    print(df.groupby(h)['No-show'].mean())


# In[13]:


Exploratory_Analysis = ['Gender','Hipertension','Alcoholism','Diabetes']
for r in Exploratory_Analysis :
    print(df.groupby(r)['No-show'].count())


# In[15]:


Exploratory_Analysis = ['Gender','Hipertension','Alcoholism','Diabetes', 'Handicap_1', 'Handicap_2', 'Handicap_3', 'Handicap_4']
for r in Exploratory_Analysis :
    print(df.groupby(r)['No-show'].count())


# In[16]:


df.hist(Exploratory_Analysis)


# In[19]:


df.hist(Exploratory_Analysis,figsize = (17,8));


# In[18]:


df.hist(figsize = (17,8));


# In[20]:


Exploratory_Analysis = ['Hipertension','Alcoholism','Diabetes', 'Handicap_1', 'Handicap_2', 'Handicap_3', 'Handicap_4']
for r in Exploratory_Analysis :
    print(df.groupby(r)['No-show'].mean())


# In[ ]:




