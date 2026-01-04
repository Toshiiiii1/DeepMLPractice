#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def make_diagonal(x):
    temp = len(x)
    # initialize a square matrix of zeros
    result = np.zeros((temp, temp))
    # fill value
    for i in range(temp):
        result[i][i] = x[i]
    return result


# In[2]:


x = np.array([1, 2, 3])
print(make_diagonal(x))

