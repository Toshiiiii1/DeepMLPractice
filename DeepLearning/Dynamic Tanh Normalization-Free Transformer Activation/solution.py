#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np

def dynamic_tanh(x: np.ndarray, alpha: float, gamma: float, beta: float) -> list[float]:
    return np.round(gamma * np.tanh(alpha * x) + beta, decimals=4)


# In[9]:


x = np.array([[[0.14115588, 0.00372817, 0.24126647, 0.22183601]]])
gamma = np.ones((4,))
beta = np.zeros((4,))
alpha = 0.5
print(dynamic_tanh(x, alpha, gamma, beta))


# In[6]:


print(np.round(gamma * np.tanh(alpha * x) + beta, decimals=4))

