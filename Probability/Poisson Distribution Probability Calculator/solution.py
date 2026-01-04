#!/usr/bin/env python
# coding: utf-8

# In[8]:


import math

def poisson_probability(k, lam):
    a = math.pow(lam, k) * math.pow(math.e, -lam)
    b = math.factorial(k)
    return round(a/b, 5)


# In[9]:


k = 3
lam = 5
print(poisson_probability(k, lam))

