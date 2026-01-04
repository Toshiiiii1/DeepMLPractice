#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        return []

    if mode == "row":
        # using list comprehension for row means
        return [sum(row) / len(row) for row in matrix]
    else:  # column mode
        # transpose the matrix using zip and calculate means
        columns = zip(*matrix)
        return [sum(col) / len(matrix) for col in columns]


# In[2]:


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = 'column'
print(calculate_matrix_mean(matrix, mode))

