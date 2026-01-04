#!/usr/bin/env python
# coding: utf-8

# In[1]:


def poly_term_derivative(c: float, x: float, n: float) -> float:
    return c * n * pow(x, n-1)


# In[2]:


poly_term_derivative(2.0, 3.0, 2.0)

