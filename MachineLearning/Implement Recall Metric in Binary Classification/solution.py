#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def recall(y_true, y_pred):
    tp, fn = 0, 0
    for i in range(len(y_true)):
        # calculate total true positive samples
        if y_true[i] == 1 and y_pred[i] == 1:
            tp += 1
        # calculate total false negative samples
        elif y_true[i] == 1 and y_pred[i] == 0:
            fn += 1
    return tp / (tp + fn) if (tp + fn) > 0 else 0


# In[5]:


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
print(recall(y_true, y_pred))

