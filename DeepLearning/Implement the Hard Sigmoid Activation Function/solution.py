#!/usr/bin/env python
# coding: utf-8

# In[7]:


def hard_sigmoid(x: float) -> float:
    return max(0, min(1, 0.2*x + 0.5))


# In[8]:


print(hard_sigmoid(0.0))

