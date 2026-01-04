#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import math

def log_softmax(scores: list) -> np.ndarray:
    # find max value of scores
    max_value = np.max(scores)
    # calculate log of sum of exponentials
    log_value = np.log(sum([np.power(math.e, x-max_value) for x in scores]))
    return np.apply_along_axis(lambda x: x - max_value - log_value, 0, scores)


# In[16]:


A = np.array([1, 2, 3])
print(log_softmax(A))

