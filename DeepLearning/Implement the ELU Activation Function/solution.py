#!/usr/bin/env python
# coding: utf-8

# In[13]:


import math

def elu(x: float, alpha: float = 1.0) -> float:
    return round(x, 4) if x > 0 else round(alpha*(pow(math.e, x) - 1), 4)


# In[14]:


print(elu(-1))

