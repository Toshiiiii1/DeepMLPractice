#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	rows, cols = np.array(a).shape
    # the total number of elements of the matrix after reshaping must be equal to the total number of elements of the original matrix.
	if rows * cols != new_shape[0] * new_shape[1]:
		return []
	reshaped_matrix = np.array(a).reshape(new_shape).tolist()
	return reshaped_matrix


# In[3]:


# input
a = [[1,2,3,4],[5,6,7,8]]
new_shape = (4, 2)
print(reshape_matrix(a, new_shape))

