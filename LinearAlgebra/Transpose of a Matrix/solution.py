#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	c = []
    # iterate over the columns of the matrix
	for i in range(len(a[0])):
        # iterrate over the rows of the matrix
        # create new row from the ith column of the original matrix
		b = [a[j][i] for j in range(len(a))]
		c.append(b)
	return c


# In[3]:


# input
a = [[1,2,3],[4,5,6]]
print(transpose_matrix(a))

