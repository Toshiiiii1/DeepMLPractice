#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np

def precision(y_true, y_pred):
    tp, fp = 0, 0
    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            tp += 1
        elif y_true[i] == 0 and y_pred[i] == 1:
            fp += 1

    return tp/(tp + fp) if (tp + fp) > 0 else 0


# In[5]:


y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
result = precision(y_true, y_pred)
print(result)

