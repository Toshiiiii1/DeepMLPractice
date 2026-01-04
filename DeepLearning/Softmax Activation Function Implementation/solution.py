#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math

def softmax(scores: list[float]) -> list[float]:
    summ = sum([math.pow(math.e, score) for score in scores])
    return [math.pow(math.e, score)/summ for score in scores]


# In[2]:


scores = [1, 2, 3]
print(softmax(scores))

