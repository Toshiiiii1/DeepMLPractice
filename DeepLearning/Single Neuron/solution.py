#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # convert parameters to numpy arrays
    features = np.array(features)
    labels = np.array(labels)
    weights = np.array(weights)

    # calculate the dot product of features and weights, add bias, and apply sigmoid function
    z = np.dot(features, weights) + bias
    probs = 1 / (1 + np.exp(-z))
    # calculate the mean squared error
    mse = np.mean(np.square(probs - labels))

    return probs, mse


# In[2]:


features = [[0.5, 1.0], [-1.5, -2.0], [2.0, 1.5]]
labels = [0, 1, 0]
weights = [0.7, -0.4]
bias = -0.1
probs, mse = single_neuron_model(features, labels, weights, bias)
print("Probabilities:", probs)
print("Mean Squared Error:", mse)

