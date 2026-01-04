#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def bhattacharyya_distance(p: list[float], q: list[float]) -> float:
    if p == [] or q == [] or len(p) != len(q):
        return 0.0
    p = np.array(p)
    q = np.array(q)
    bc = sum(np.sqrt(p * q))
    bd = -np.log(bc)
    return round(bd, 4)


# In[12]:


p = [0.1, 0.2, 0.3, 0.4]
q = [0.4, 0.3, 0.2, 0.1]
print(bhattacharyya_distance(p, q))

