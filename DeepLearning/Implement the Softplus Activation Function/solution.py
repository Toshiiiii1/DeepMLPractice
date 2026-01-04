#!/usr/bin/env python
# coding: utf-8

# In[6]:


import math

def softplus(x: float) -> float:
    return round(math.log(1 + pow(math.e, x)), 4)


# In[7]:


softplus(2)

