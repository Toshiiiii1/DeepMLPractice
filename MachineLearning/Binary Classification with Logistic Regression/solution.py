#!/usr/bin/env python
# coding: utf-8

# In[90]:


import numpy as np

def predict_logistic(X: np.ndarray, weights: np.ndarray, bias: float) -> np.ndarray:
    # linear combination between X and weights
    z = np.dot(X, weights) + bias
    # apply sigmoid activation function
    probs = np.apply_along_axis(func1d=lambda z: 1 / (1 + pow(np.e, -z)), axis=0, arr=z)
    # convert probs to labels
    labels = np.where(probs < 0.5, 0, 1)

    return labels


# In[91]:


x = np.array([[0, 0], [0.1, 0.1], [-0.1, -0.1]])
weights = np.array([1, 1])
bias = 0
print(predict_logistic(x, weights=weights, bias=bias))

