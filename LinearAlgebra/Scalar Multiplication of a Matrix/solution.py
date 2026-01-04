#!/usr/bin/env python
# coding: utf-8

# In[1]:


def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = [[scalar * i for i in row] for row in matrix]
	return result


# In[2]:


matrix = [[1, 2], [3, 4]]
scalar = 2
print(scalar_multiply(matrix, scalar))

