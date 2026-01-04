#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def accuracy_score(y_true, y_pred):
    # y_true==y_pred returns a boolean array where True indicates a match
    # np.count_nonzero counts the number of True values in the boolean array
    return np.count_nonzero(y_true==y_pred)/len(y_true)


# In[2]:


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 0, 1, 0, 1])
print(accuracy_score(y_true, y_pred))

