#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def dice_score(y_true, y_pred):
    if len(y_true) == 0 or len(y_pred) == 0:
        return 0.0
    tp = np.sum(y_true & y_pred)
    fp, fn = 0, 0
    for i in range(len(y_true)):
        if y_true[i] == 0 and y_pred[i] == 1:
            fp += 1
        elif y_true[i] == 1 and y_pred[i] == 0:
            fn += 1
    res = (2*tp)/(2*tp + fp + fn) if 2*tp + fp + fn != 0 else 0.0

    return round(res, 3)


# In[13]:


y_true = np.array([1, 1, 0, 0])
y_pred = np.array([1, 1, 0, 0])
print(dice_score(y_true, y_pred))

