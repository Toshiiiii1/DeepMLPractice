#!/usr/bin/env python
# coding: utf-8

# In[51]:


import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    loss = np.sum(true_labels * np.log(predicted_probs), axis=1)
    mean_logg = -np.mean(loss)
    result = round(mean_logg, 4)
    return result if result != 0.0 else -result


# In[52]:


pred = np.array([[0.7, 0.2, 0.1], [0.3, 0.6, 0.1]])
true = np.array([[1, 0, 0], [0, 1, 0]])
print(compute_cross_entropy_loss(pred, true))

