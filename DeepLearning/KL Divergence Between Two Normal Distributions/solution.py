#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
    # calculate the KL divergence between two normal distributions
    # p ~ N(mu_p, sigma_p^2)
    # q ~ N(mu_q, sigma_q^2)
    return np.log(sigma_q / sigma_p) + (sigma_p**2 + (mu_p - mu_q)**2) / (2 * sigma_q**2) - 0.5


# In[15]:


mu_p = 0.0
sigma_p = 1.0

mu_q = 1.0
sigma_q = 1.0

print(kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q))

