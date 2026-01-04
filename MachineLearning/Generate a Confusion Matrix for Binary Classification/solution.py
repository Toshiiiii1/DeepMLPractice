#!/usr/bin/env python
# coding: utf-8

# In[7]:


from collections import Counter

def confusion_matrix(data):
    tp, fp, fn, tn = 0, 0, 0, 0
    for pair in data:
        if pair[0] == 1 and pair[1] == 1:
            tp += 1
        elif pair[0] == 1 and pair[1] == 0:
            fn += 1
        elif pair[0] == 0 and pair[1] == 1:
            fp += 1
        elif pair[0] == 0 and pair[1] == 0:
            tn += 1

    return [[tp, fn], [fp, tn]]


# In[8]:


data = [[1, 1], [1, 0], [0, 1], [0, 0], [0, 1]]
print(confusion_matrix(data))

