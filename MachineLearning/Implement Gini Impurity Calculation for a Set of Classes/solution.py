#!/usr/bin/env python
# coding: utf-8

# In[13]:


import numpy as np

def gini_impurity(y):
    # calculate prob of each class in y
    probs = np.unique(y, return_counts=True)[1]/len(y)
    # calculate gini impurity
    gini = 1 - np.sum(probs**2)
    return round(gini, 3)


# In[15]:


y = [0, 1, 1, 1, 0]
print(gini_impurity(y))

