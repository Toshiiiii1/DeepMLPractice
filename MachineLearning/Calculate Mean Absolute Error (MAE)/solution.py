#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np

def mae(y_true, y_pred):
    return round(np.mean(np.absolute(y_true - y_pred)), 3)


# In[8]:


y_true = np.array([3, -0.5, 2, 7])
y_pred = np.array([2.5, 0.0, 2, 8])
print(mae(y_true, y_pred))

