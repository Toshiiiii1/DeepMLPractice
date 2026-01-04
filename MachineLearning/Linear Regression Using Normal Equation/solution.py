#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # convert X and y to numpy arrays
    np_X = np.array(X)
    np_y = np.array(y)
    return np.round(np.matmul(np.matmul(np.linalg.inv(np.matmul(np_X.T, np_X)), np_X.T), y), decimals=4)


# In[3]:


X = [[1, 1], [1, 2], [1, 3]]
y = [1, 2, 3]
print(linear_regression_normal_equation(X, y))

