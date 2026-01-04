#!/usr/bin/env python
# coding: utf-8

# In[2]:


import math

def sigmoid(z: float) -> float:
    return round(1/(1+math.pow(math.e, -z)), 4)


# In[3]:


z = 0
print(sigmoid(z))

