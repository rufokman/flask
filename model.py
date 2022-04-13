#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display
diam = pd.read_csv('diamonds.csv', index_col = 'Unnamed: 0')


# In[2]:


diam.drop(diam[diam['x'] == 0].index, inplace=True)
diam.drop(diam[diam['y'] == 0].index, inplace=True)
diam.drop(diam[diam['z'] == 0].index, inplace=True)


# In[5]:


diam.drop(['cut','color','clarity'], axis=1,inplace=True)


# In[ ]:





# #### продаммируем cut

# ### model
# 

# In[9]:


from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split


# In[10]:


X_train, X_test, y_train, y_test = train_test_split(diam.drop('price', axis=1), diam.price, random_state=42)
diam_net = ElasticNet()
diam_net.fit(X_train, y_train)


# In[13]:


import joblib

joblib.dump(diam_net, "diam_net.pkl")


# In[ ]:




