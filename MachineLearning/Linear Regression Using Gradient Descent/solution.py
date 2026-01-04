#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def linear_model(theta, x):
    return sum([theta[i] * x[i] for i in range(len(theta))])

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    # initialize theta
    theta = np.zeros((n,))

    for _ in range(iterations):
        new_theta = np.zeros((n,))
        for i in range(n):
            """
            sum([(linear_model(theta, X[j]) - y[j]) * X[j][i] for j in range(m)]) is sigma fomular
            """
            new_theta[i] = theta[i] - sum([(linear_model(theta, X[j]) - y[j]) * X[j][i] for j in range(m)])/m * alpha
        theta = new_theta.copy()

    return theta

"""
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
    m, n = X.shape
    theta = np.zeros((n,))

    for _ in range(iterations):
        pred = X.dot(theta)
        error = pred - y
        gradient = X.T.dot(error)/m
        theta = theta - alpha * gradient
    return theta
"""


# In[2]:


X = np.array([[1, 1], [1, 2], [1, 3]])
y = np.array([1, 2, 3])
alpha = 0.01
iterations = 1000
theta = linear_regression_gradient_descent(X, y, alpha, iterations)
print("Theta:", theta)

