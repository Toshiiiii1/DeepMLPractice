#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np

def global_avg_pool(x: np.ndarray) -> np.ndarray:
    return np.average(x, axis=(0, 1))


# In[ ]:


'''
Example:
data = np.array([
  [[0, 1],
   [2, 3]],

  [[4, 5],
   [6, 7]]
])

axis = 0 inlcudes: (0, 4), (1, 5), (2, 6), (3, 7)
axis = 1 includes: (0, 2), (1, 3), (4, 6), (5, 7)
axis = 2 includes: (0, 1), (2, 3), (4, 5), (6, 7)
axis = (0, 1) includes: (0, 2, 4, 6), (1, 3, 5, 7)
axis = (1, 2) includes: (0, 1, 2, 3), (4, 5, 6, 7)
axis = (0, 2) includes: (0, 1, 4, 5), (2, 3, 6, 7)
'''

x = np.array([
  [[ 1,  2,  3],
   [ 4,  5,  6]],

  [[ 7,  8,  9],
   [10, 11, 12]]
])

print(global_avg_pool(x))

