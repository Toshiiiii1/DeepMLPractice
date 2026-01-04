#!/usr/bin/env python
# coding: utf-8

# In[5]:


def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
    if len(a) != len(b):
        return -1
    return [a[i] + b[i] for i in range(len(a))]


# In[7]:


a = [1, 3, 3]
b = [4, 5]
print(vector_sum(a, b))

