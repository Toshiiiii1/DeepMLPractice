#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math

def swish(x: float) -> float:
    return round(x * (1/(1+pow(math.e, -x))), 4)


# In[9]:


print(swish(1))

