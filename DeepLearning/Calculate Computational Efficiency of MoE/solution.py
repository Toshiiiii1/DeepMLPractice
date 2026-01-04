#!/usr/bin/env python
# coding: utf-8

# In[2]:


def compute_efficiency(n_experts, k_active, d_in, d_out):
    flop_dense = n_experts * d_in * d_out
    flop_moe = k_active * d_in * d_out

    return (flop_dense - flop_moe) / flop_dense * 100


# In[3]:


compute_efficiency(1000, 2, 512, 512)

