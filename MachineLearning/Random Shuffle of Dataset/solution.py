#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def shuffle_data(X, y, seed=None):
    if seed:
        np.random.seed(seed)
    indexs = np.arange(len(X))
    np.random.shuffle(indexs)
    new_X = np.array([X[i] for i in indexs])
    new_y = np.array([y[i] for i in indexs])

    return new_X, new_y


# In[10]:


X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8]])
y = np.array([1, 2, 3, 4])
print(shuffle_data(X, y, seed=42))

