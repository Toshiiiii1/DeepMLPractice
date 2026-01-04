#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def jaccard_index(y_true, y_pred):
    if len(y_true) == 0 or len(y_pred) == 0:
        return 0.0
    # uee and operator to calculate intersection between two binary sets
    inter = sum(y_pred & y_true)
    # uee or operator to calculate intersection between two binary sets
    union = sum(y_pred | y_true)
    return inter / union if union != 0 else 0.0


# In[19]:


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
print(jaccard_index(y_true, y_pred))

