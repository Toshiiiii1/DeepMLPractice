#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    num_samples = len(X)
    result = []
    for start in range(0, num_samples, batch_size):
        '''
        end index keep track the end position of batch's element
        even the remain of the dataset
        '''
        end = min(start + batch_size, num_samples)
        if y is not None:
            result.append([X[start:end].tolist(), y[start:end].tolist()])
        else:
            result.append([X[start:end].tolist()])
    return result


# In[3]:


X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
result = batch_iterator(X, y, batch_size)
for batch in result:
    print(batch[0], batch[1])

