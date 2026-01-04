#!/usr/bin/env python
# coding: utf-8

# In[5]:


def prelu(x: float, alpha: float = 0.25) -> float:
    if x > 0:
        return x
    else:
        return x * alpha


# In[6]:


print(prelu(-2.0, alpha=0.25))

