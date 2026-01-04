#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math

def selu(x: float) -> float:
    alpha = 1.6732632423543772
    scale = 1.0507009873554804
    if x > 0:
        return round(scale * x, 4)
    else:
        return round(scale * alpha * (pow(math.e, x) - 1), 4)


# In[6]:


print(selu(-1.0))

