#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np

def calculate_contrast(img) -> int:
    return np.max(img) - np.min(img)


# In[7]:


img = np.array([[0, 50], [200, 255]])
print(calculate_contrast(img))

