#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np

def residual_block(x: np.ndarray, w1: np.ndarray, w2: np.ndarray) -> np.ndarray:
    z1 = np.dot(x, w1)
    z1 = np.array(list(map(lambda x: max(0, x), z1)))
    z2 = np.dot(z1, w2)
    z2 = np.array(list(map(lambda x: max(0, x), z2)))
    y = np.array(list(map(lambda x: max(0, x), z2 + x)))
    return y


# In[19]:


x = np.array([1.0, 2.0])
w1 = np.array([[1.0, 0.0], [0.0, 1.0]])
w2 = np.array([[0.5, 0.0], [0.0, 0.5]])
print(residual_block(x, w1, w2))

