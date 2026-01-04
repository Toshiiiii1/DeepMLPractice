#!/usr/bin/env python
# coding: utf-8

# In[5]:


def leaky_relu(z: float, alpha: float = 0.01) -> float|int:
    return z if z > 0 else alpha * z


# In[6]:


print(leaky_relu(0)) 
print(leaky_relu(1))
print(leaky_relu(-1)) 
print(leaky_relu(-2, alpha=0.1))

