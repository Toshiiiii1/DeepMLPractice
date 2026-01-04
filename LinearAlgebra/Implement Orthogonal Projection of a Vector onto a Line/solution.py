#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np

def orthogonal_projection(v, L):
    v = np.array(v)
    L = np.array(L)
    return np.dot(v, L) / np.dot(L, L) * L


# In[8]:


v = [3, 4]
L = [1, 0]
print(orthogonal_projection(v, L))

