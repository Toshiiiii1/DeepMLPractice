#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # check if the number of columns in a equals the length if vector b
    if len(a[0]) != len(b):
        return -1

    '''
    - sum(row[i] * b[i] for i in range(len(b))): calculates the dot product of each row in matrix a with vector b.
    - [ ... for row in a]: iterates through each row of matrix a.
    '''
    return [sum(row[i] * b[i] for i in range(len(b))) for row in a]


# In[5]:


# input
a = [[1, 2], [2, 4]]
b = [1, 2]
print(matrix_dot_vector(a, b))

