#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


Bitcoin = pd.read_csv("BTC-EUR.csv", index_col='Date', inplace=True)


# In[2]:


Bitcoin.head()


# In[84]:


Bitcoin['Close'].plot(figsize=(12, 6))


# In[93]:


Bitcoin.loc['2021-11':'2022-01','Close'].resample('M').plot(figsize=(12, 6))


# In[95]:


Bitcoin.loc['2021-11':'2022-01','Close'].resample('M').mean().plot(figsize=(12, 6))


# In[ ]:





# In[107]:


plt.figure(figsize=(12, 8))

Bitcoin.loc['2021', 'Close'].plot()
Bitcoin.loc['2021', 'Close'].resample('M').mean().plot(label='Moyenne par mois', lw=3, ls=':', alpha=0.8)
Bitcoin.loc['2021', 'Close'].resample('W').mean().plot(label='Moyenne par semaines', lw=2, ls='--', alpha=0.8)


# In[117]:


m=Bitcoin['Close'].resample('W').agg(['mean','std','min','max'])
m.head()


# In[126]:


plt.figure(figsize=(12, 8))
m['mean']['2021':'2022'].plot(label='moyenne par semaine')
plt.fill_between(m.index, m['max'], m['min'], alpha=0.3, label='min-max par semaine')
plt.legend()
plt.show()


# In[129]:


plt.figure(figsize=(12, 8))
Bitcoin.loc['2021':'2022','Close'].plot()
Bitcoin.loc['2021':'2022','Close'].rolling(windows=7).mean().plot(label='moving average')


# In[ ]:




