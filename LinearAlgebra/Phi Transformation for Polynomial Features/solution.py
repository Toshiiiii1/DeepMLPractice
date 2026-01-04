#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np

def phi_calculate(x, degree):
    result = []
    for i in range(degree+1):
        result.append(np.pow(x, i))
    return result

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
    result = []
    if degree >= 0:
        for i in data:
            temp = []
            for j in range(degree+1):
                temp.append(np.pow(i, j))
            result.append(temp)

    return result


# In[13]:


data = [1.0, 2.0]
degree = 2
print(phi_transform(data, degree))

