#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math

def min_max_scaling(data):
    min_vals = np.min(data, axis=0)
    max_vals = np.max(data, axis=0)

    return (data - min_vals) / (max_vals - min_vals)

def standard_scaling(data):
    means = np.mean(data, axis=0)
    stds = np.std(data, axis=0)

    return (data - means)/stds

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    standardized_data = standard_scaling(data)
    normalized_data = min_max_scaling(data)
    return standardized_data, normalized_data


# In[3]:


data = np.array([[1, 2], [3, 4], [5, 6]])
result = feature_scaling(data)
for i in result:
    print(i)

