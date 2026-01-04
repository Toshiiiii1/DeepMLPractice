#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

def cross_product(a, b):
    return np.cross(a, b)


# In[6]:


a = [1, 0, 0]
b = [0, 1, 0]
print(cross_product(a, b))

