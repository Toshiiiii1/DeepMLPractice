#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np

def compressed_col_sparse_matrix(dense_matrix):
    cols = len(dense_matrix[0])
    rows = len(dense_matrix)

    vals, row_idx, col_ptr = [], [], [0]

    for i in range(cols):
        count = 0
        for j in range(rows):
            if dense_matrix[j][i] != 0:
                vals.append(dense_matrix[j][i])
                row_idx.append(j)
                count += 1
        col_ptr.append(col_ptr[-1] + count)

    return vals, row_idx, col_ptr


# In[11]:


dense_matrix = [
    [0, 0, 3, 0],
    [1, 0, 0, 4],
    [0, 2, 0, 0]
]

vals, row_idx, col_ptr = compressed_col_sparse_matrix(dense_matrix)
print(vals)
print(row_idx)
print(col_ptr)

