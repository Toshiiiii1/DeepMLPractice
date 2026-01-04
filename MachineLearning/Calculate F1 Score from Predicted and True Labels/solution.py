#!/usr/bin/env python
# coding: utf-8

# In[20]:


def calculate_f1_score(y_true, y_pred):
    tp, fp, fn = 0, 0, 0
    for i in range(len(y_true)):
        if y_true[i] == 1 and y_pred[i] == 1:
            tp += 1
        elif y_true[i] == 0 and y_pred[i] == 1:
            fp += 1
        elif y_true[i] == 1 and y_pred[i] == 0:
            fn += 1
    try:
        precision = tp/(tp + fp)
        recall = tp/(tp + fn)
        f1 = (2 * precision * recall)/(precision + recall)
    except:
        f1 = 0.0
    return round(f1, 3)


# In[21]:


y_true = [1, 0, 1, 1, 0]
y_pred = [1, 0, 0, 1, 1]
print(calculate_f1_score([0, 0, 0, 0], [1, 1, 1, 1]))

