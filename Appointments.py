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


df.rename(columns = {'Hipertension': 'Hypertension', 'Handcap': 'Handicap', 'No-Show':'No_Show'}, inplace = True)


# In[5]:


df.columns


# In[6]:


df.rename(columns = {'Hipertension': 'Hypertension'}, inplace = True)


# In[7]:


df.rename(columns = {'Handcap': 'Handicap'}, inplace = True)


# In[10]:


df.rename(columns = {'No-Show': 'No_Show'}, inplace = True)


# In[11]:


df.columns


# In[ ]:





# In[12]:


no_show = df["No-show"].value_counts()
print(no_show)


# In[13]:


Pct_no_show = no_show["Yes"]/ no_show.sum() * 100
print("Percent who didn't show up to their appointment:",Pct_no_show )


# In[19]:


df.[No_show].hist();


# In[26]:


df.hist(column='No-show' bins=50)


# In[29]:


df.hist(column='Age', bins=50)


# In[30]:


df["Gender"].value_counts()


# In[35]:


Exploratory_Analysis = ['Gender','Hypertension','Alcoholism','Diabetes']
for r in Exploratory_Analysis :
    print(df.groupby(r)['No-show'].mean())


# In[ ]:





# In[32]:


df.columns


# In[37]:


Exploratory_Analysis = ['Gender','Hypertension','Alcoholism','Diabetes']
for r in Exploratory_Analysis :
    print(df.groupby(r)['No-show'].mean())


# In[38]:


min_age = df.Age.min()
print("Min Age:", min_age)
max_age = df.Age.max()
print("Max Age:", max_age)


# In[39]:


df = df[(df.Age >= 0) & (df.Age <= 100)]


# In[40]:


df.groupby('SMS_received')['No-show'].mean()


# In[47]:


df.groupby('SMS_received')['No-show'].mean()


# In[46]:


df.columns


# In[48]:


no_show = df["No-show"].value_counts()
print(no_show)


# In[49]:


Percent_no_show = no_show["Yes"]/ no_show.sum() * 100
print("Percent who didn't show up to their appointment:",Percent_no_show )


# In[50]:


df['No-show'].replace("No", 0,inplace=True)
df['No-show'].replace("Yes", 1,inplace=True)


# In[51]:


df["Gender"].value_counts()


# In[52]:


Exploratory_Analysis = ['Gender','Hypertension','Alcoholism','Diabetes']
for r in Exploratory_Analysis :
    print(df.groupby(r)['No-show'].mean())


# In[53]:


df.hist(column='No-show')


# In[54]:


df.groupby('SMS_received')['No-show'].mean()


# In[57]:


AwaitingTime = df["AppointmentDay"].sub(df["ScheduledDay"], axis=0)


# In[59]:


df["AwaitingTime"] = df["AppointmentDay"].sub(df["ScheduledDay"], axis=0)
df["AwaitingTime"] = (df["AwaitingTime"] / np.timedelta64(1, 'D')).abs()


# In[60]:


df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay'])
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay'])


# In[61]:


df['AwaitingTime'] = df["AppointmentDay"].sub(df["ScheduledDay"], axis=0)


# In[62]:


df["AwaitingTime"] = (df["AwaitingTime"] / np.timedelta64(1, 'D')).abs()


# In[64]:


df["AwaitingTime"].mean()


# In[65]:


cat = [0, 20, 40, 60, 100]
age_groups = df.groupby(pd.cut(df.Age, cat))
age_groups["No-show"].mean()


# In[66]:


df.hist(Exploratory_Analysis)


# In[1]:


df.hist(figsize = (17,8));


# In[2]:


df.hist(figsize = (17,8));


# In[1]:


df.hist(figsize = (17,8));


# In[ ]:





# In[2]:


df.info()


# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


df = pd.read_csv("h:/downloads/noshowappointments-kagglev2-may-2016.csv")


# In[5]:


df.hist(figsize = (17,8));


# In[7]:


NoShow = df.NoShow == True
Showed = df.NoShow == False


# In[8]:


NoShow = df.No-show == True
Showed = df.No-show == False


# In[9]:


df.info()


# In[10]:


NoShow = df.No-show == True
Showed = df.No-show == False


# In[11]:


df.rename(columns={'No-show': 'NoShow'}, inplace=True)


# In[12]:


df = df.replace({'NoShow': {'Yes': True, 'No': False}})


# In[13]:


df.NoShow = df.NoShow.astype(int)


# In[14]:


NoShow = df.NoShow == True
Showed = df.NoShow == False


# In[15]:


def didnt_show_mean ():
 return df.Age[NoShow].mean()


# In[16]:


didnt_show_mean ()


# In[17]:


def showed_up_mean ():
 return df.Age[Showed].mean()


# In[18]:


showed_up_mean ()


# In[19]:


df.Age[Showed].hist(alpha=0.5, bins=20, label = 'Showed Up',color = 'green')
df.Age[NoShow].hist(alpha=0.5,bins=20, label = 'No Show',color = 'red')
plt.legend()
plt.xlabel('Patient Age')
plt.ylabel('# of Patients');


# In[20]:


df['Age'].hist()
plt.xlabel('Patient Age')
plt.ylabel('# of Patients');


# In[21]:


df.groupby('Gender').NoShow.mean().plot(kind='bar')
plt.xlabel('Patient Gender')
plt.ylabel('Avg "No-Show" Occurrence');


# In[24]:


df.Gender[Showed].value_counts().plot(kind = 'bar',alpha=0.5,figsize = (6,6),
label = 'Showed Up',color='green')
df.Gender[NoShow].value_counts().plot(kind = 'bar', alpha=0.5,figsize = (6,
6),label = 'No Show', color='red')
plt.legend()
plt.xlabel('Patient Gender')
plt.ylabel('# of Patients');


# In[26]:


df.Neighbourhood[Showed].value_counts().plot(kind = 'bar',alpha=0.5,figsize =
(30,20),label = 'Showed Up',color='purple')
df.Neighbourhood[NoShow].value_counts().plot(kind = 'bar', alpha=0.5,figsize = (30,20),label = 'No Show', color='red')
plt.legend()
plt.xlabel('Patients Neighborhood')
plt.ylabel('"No Show Counts');


# In[27]:


df.info()


# In[28]:


Exploratory_Analysis = ['Gender','Hipertension','Alcoholism','Diabetes', 'Handcap']
for r in Exploratory_Analysis :
    print(df.groupby(r)['NoShow'].mean())


# In[30]:


df.hist(figsize=8,8).(Exploratory_Analysis)


# In[33]:


df.(Exploratory_Analysis.figsize=8,8)


# In[35]:


df.[Exploratory_Analysis].hist(figsize=8,8)


# In[38]:


df.Exploratory_Analysis.hist(figsize=8)


# In[39]:


df.hist(Exploratory_Analysis, figsize 8,8)


# In[40]:


df.hist(Exploratory_Analysis, (figsize 8,8))


# In[41]:


df.hist(Exploratory_Analysis)


# In[45]:


df.hist(Exploratory_Analysis figsize=8,8)


# In[ ]:





# In[46]:


df.rename(columns = {'Hipertension': 'Hypertension', 'Handcap': 'Handicap', 'No-Show':'No_Show'}, inplace = True)


# In[47]:


df.hist(Exploratory_Analysis)


# In[48]:


Exploratory_Analysis = ['Gender','Hypertension','Alcoholism','Diabetes', 'Handicap']
for r in Exploratory_Analysis :
    print(df.groupby(r)['NoShow'].mean())


# In[49]:


df.hist(Exploratory_Analysis)


# In[1]:


df.head()


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv("h:/downloads/noshowappointments-kagglev2-may-2016.csv")


# In[ ]:


df.head()


# In[4]:


df = pd.read_csv("h:/downloads/noshowappointments-kagglev2-may-2016.csv")


# In[5]:


df = pd.read_csv("h:/downloads/noshowappointments-kagglev2-may-2016.csv")


# In[6]:


df.head()


# In[8]:


df.drop(['PatientId','AppointmentID'],axis=1,inplace=True)


# In[9]:


df.head()


# In[10]:


sum(df.duplicated())


# In[ ]:




