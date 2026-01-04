#!/usr/bin/env python
# coding: utf-8

# In[1]:


def calculate_covariance_matrix(matrix: list[list[float]]) -> list[list[float]]:
    # matrix parameter is a set of vectors (features or columns), not "normal" matrix
    # len(matrix) return number of columns instead of rows

    # calculate the mean of each column
    means = [sum(row)/len(row) for row in matrix]

    # create a covariance matrix full 0s
    result = [[0] * len(matrix) for _ in range(len(matrix))]

    # number of rows of each column
    m = len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            """
            - i=0, j=0: cov(X1, X1)
            - i=0, j=1: cov(X1, X2)
            ...
            """
            result[i][j] = sum([(matrix[i][k] - means[i]) * (matrix[j][k] - means[j]) for k in range(m)])/(m-1)

    return result


# In[2]:


matrix = [[1, 2, 3], [4, 5, 6]]
print(calculate_covariance_matrix(matrix))

