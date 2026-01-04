#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def to_categorical(x, n_col=None):
    num_row = len(x)
    # get unique values in x
    values = np.unique(x)
    if n_col is None:
        n_col = len(values)

 	# initialize one-hot encoded matrix
    one_hot = np.zeros((num_row, n_col))

    # fill values in one-hot encoded matrix
    for i in range(num_row):
        one_hot[i][x[i]] = 1

    return one_hot


# In[2]:


x = np.array([0, 1, 2, 1, 0])
print(to_categorical(x))

