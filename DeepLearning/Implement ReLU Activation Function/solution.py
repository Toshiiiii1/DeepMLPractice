#!/usr/bin/env python
# coding: utf-8

# In[2]:


def relu(z: float) -> float:
	return max(0, z)


# In[3]:


print(relu(0)) 
print(relu(1)) 
print(relu(-1))

