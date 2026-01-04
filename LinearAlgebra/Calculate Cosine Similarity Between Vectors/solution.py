#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    l2_norm_v1 = np.sqrt(sum(i**2 for i in v1))
    l2_norm_v2 = np.sqrt(sum(i**2 for i in v2))
    return dot_product/(l2_norm_v1 * l2_norm_v2)


# In[10]:


v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])
print(cosine_similarity(v1, v2))

