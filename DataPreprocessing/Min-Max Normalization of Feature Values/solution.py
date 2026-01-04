#!/usr/bin/env python
# coding: utf-8

# In[8]:


def min_max(x: list[int]) -> list[float]:
    min_v, max_v = min(x), max(x)
    if min_v == max_v:
        return [0.0] * len(x)
    return list(map(lambda x: (x - min_v) / (max_v - min_v), x))


# In[6]:


print(min_max([1, 2, 3, 4, 5]))

