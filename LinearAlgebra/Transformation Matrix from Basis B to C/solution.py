#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
    B, C = np.array(B), np.array(C)

    return np.linalg.inv(C) @ B


# In[4]:


B = [[1, 0, 0], 
             [0, 1, 0], 
             [0, 0, 1]]
C = [[1, 2.3, 3], 
             [4.4, 25, 6], 
             [7.4, 8, 9]]
print(transform_basis(B, C))

