#!/usr/bin/env python
# coding: utf-8

# In[1]:


def softsign(x: float) -> float:
    return round(x / (1 + abs(x)), 4)


# In[2]:


print(softsign(1))

