#!/usr/bin/env python
# coding: utf-8

# In[83]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[84]:


dfset = pd.read_csv('UberDataset.csv')
dfset


# In[85]:


dfset.head()


# In[86]:


dfset.info()


# In[87]:


dfset.shape


# # Data Pre-Processing

# In[88]:


dfset['PURPOSE'].fillna("NOT", inplace = True)


# In[89]:


dfset.head()


# In[90]:


dfset['START_DATE'] = pd.to_datetime(dfset['START_DATE'], errors = 'coerce')

dfset['END_DATE'] = pd.to_datetime(dfset['END_DATE'], errors = 'coerce')


# In[91]:


dfset.info()


# In[92]:


from datetime import datetime

dfset['date'] = pd.DatetimeIndex(dfset['START_DATE']).date

dfset['time'] = pd.DatetimeIndex(dfset['START_DATE']).hour


# In[93]:


dfset.head()


# In[94]:


dfset['day-night'] = pd.cut(x=dfset['time'], bins = [0,10,15,19,24], labels = ['Morning','Afternoon','Evening','Night'])


# In[95]:


dfset.head()


# In[96]:


dfset.dropna(inplace = True)


# In[97]:


dfset.shape


# # DATA VISUALIZATION

# In[98]:


plt.figure(figsize=(20,5))

plt.subplot(1,2,1)

sns.countplot(dfset['CATEGORY'])
plt.xticks(rotation=90)

plt.subplot(1,2,2)
sns.countplot(dfset['PURPOSE'])


# In[ ]:


sns.countplot(dfset['day-night'])


# In[ ]:


dfset.head(10)


# In[102]:


dfset['MONTH'] = pd.DatetimeIndex(dfset['START_DATE']).month

month_label = {1.0: 'Jan', 2.0: 'Feb', 3.0: 'Mar', 4.0: 'Apr',
              5.0: 'May', 6.0: 'June', 7.0: 'July', 8.0: 'Aug',
              9.0: 'Sep', 10.0: 'Oct', 11.0: 'Nov', 12.0: 'Dec'}

dfset['MONTH'] = dfset.MONTH.map(month_label)

mon = dfset.MONTH.value_counts(sort=False)


# In[103]:


dfset.head(10)


# In[104]:


df = pd.DataFrame({
    "MONTHS": mon.values,
    "VALUE-COUNT": dfset.groupby('MONTH', sort=False)['MILES'].max()
})

p = sns.lineplot(data=df)
p.set(xlabel = "MONTHS", ylabel = "VALUE COUNT")


# In[107]:


dfset['DAY'] = dfset.START_DATE.dt.weekday

day_label = {
    0: 'Mon', 1: 'Tue', 2: 'Wed', 3: 'Thurs', 4: 'Fri', 5: 'Sat', 6: 'Sun'}

dfset['DAY'] = dfset['DAY'].map(day_label)


# In[108]:


dfset.head()


# In[109]:


day_label = dfset.DAY.value_counts()

sns.barplot(x=day_label.index, y=day_label)
plt.xlabel('DAY')
plt.ylabel('COUNT')


# In[110]:


sns.boxplot(dfset['MILES'])


# In[111]:


sns.boxplot(dfset[dfset['MILES']<100]['MILES'])


# In[114]:


sns.boxplot(dfset[dfset['MILES']<40]['MILES'])


# In[115]:


sns.distplot(dfset[dfset['MILES']<40]['MILES'])


# In[ ]:




