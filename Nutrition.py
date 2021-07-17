#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd

df = pd.read_csv("FoodList.csv", encoding = 'utf-8')
d_f=pd.DataFrame(df)
d_f


# In[37]:


df_drop = d_f.dropna(axis = 1)


# In[38]:


df_drop


# In[ ]:




