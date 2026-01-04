#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def kernel_function(x1, x2):
    # linear kernel = dot product
    return np.dot(x1, x2)


# In[3]:


x1 = np.array([1, 2, 3])
x2 = np.array([4, 5, 6])

result = kernel_function(x1, x2)
print(result)

