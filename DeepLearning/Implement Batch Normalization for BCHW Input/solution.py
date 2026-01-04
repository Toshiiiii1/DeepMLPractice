#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import math

def batch_normalization(X: np.ndarray, gamma: np.ndarray, beta: np.ndarray, epsilon: float = 1e-5) -> np.ndarray:
    # B, C, H, W  = X.shape
    # means = []
    # for channel in range(C):
    #     total = 0.0
    #     for batch in range(B):
    #         for h in range(H):
    #             for w in range(W):
    #                 total += X[batch][channel][h][w]
    #     means.append(total/(B*H*W))

    # vars = []
    # for channel in range(C):
    #     total = 0.0
    #     for batch in range(B):
    #         for h in range(H):
    #             for w in range(W):
    #                 total += pow(X[batch][channel][h][w] - means[channel], 2)
    #     vars.append(total/(B*H*W))

    # for channel in range(C):
    #     for batch in range(B):
    #         for h in range(H):
    #             for w in range(W):
    #                 nume = X[batch][channel][h][w] - means[channel]
    #                 deno = math.sqrt(vars[channel] + 1e-5)
    #                 X[batch][channel][h][w] = nume/deno

    means = np.mean(X, axis=(0, 2, 3), keepdims=True) # Output: [1, C, 1, 1]
    vars = np.var(X, axis=(0, 2, 3), keepdims=True) # Output: [1, C, 1, 1]

    X_norm = (X - means) / np.sqrt(vars + epsilon)

    return gamma*X_norm + beta


# In[37]:


B, C, H, W = 2, 2, 2, 2
np.random.seed(42)
X = np.random.randn(B, C, H, W)
gamma = np.ones(C).reshape(1, C, 1, 1)
beta = np.zeros(C).reshape(1, C, 1, 1)
print(batch_normalization(X, gamma, beta))

