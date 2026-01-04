#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np

def r_squared(y_true, y_pred):
    ssr = np.sum((y_true - y_pred) ** 2)
    sst = np.sum((y_true - np.mean(y_true)) ** 2)

    return 1 - (ssr / sst)


# In[7]:


y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([1.1, 2.1, 2.9, 4.2, 4.8])
print(r_squared(y_true, y_pred))

