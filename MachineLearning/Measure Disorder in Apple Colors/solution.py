#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np

def disorder(apples: list) -> float:
    value_counts = np.unique(apples, return_counts=True)
    return 1 - sum(pow(value_counts[1] / sum(value_counts[1]), 2))


# In[18]:


print(disorder([1,1,0,0]))

