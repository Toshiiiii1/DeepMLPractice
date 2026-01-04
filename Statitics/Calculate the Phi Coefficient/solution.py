#!/usr/bin/env python
# coding: utf-8

# In[12]:


import math

def phi_corr(x: list[int], y: list[int]) -> float:
    counts = {
        (0, 0): 0,
        (0, 1): 0,
        (1, 0): 0,
        (1, 1): 0,
    }

    for xi, yi in zip(x, y):
        counts[(xi, yi)] += 1

    x00 = counts[(0, 0)]
    x01 = counts[(0, 1)]
    x10 = counts[(1, 0)]
    x11 = counts[(1, 1)]

    return (x00*x11 - x01*x10)/math.sqrt((x00+x01)*(x10+x11)*(x00+x10)*(x01+x11))


# In[ ]:


phi_corr([1, 1, 0, 0], [0, 0, 1, 1])

