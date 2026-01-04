#!/usr/bin/env python
# coding: utf-8

# In[11]:


import numpy as np 
def descriptive_statistics(data):
    mean = np.mean(data)
    median = np.median(data)
    variance = np.var(data)
    std_dev = np.std(data)
    percentiles = [np.percentile(data, 25), np.percentile(data, 50), np.percentile(data, 75)]
    iqr = percentiles[-1] - percentiles[0]

    unique_counts = np.unique(data, return_counts=True)
    index = np.argmax(unique_counts[1])
    mode = unique_counts[0][int(index)]
    stats_dict = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": np.round(variance,4),
        "standard_deviation": np.round(std_dev,4),
        "25th_percentile": percentiles[0],
        "50th_percentile": percentiles[1],
        "75th_percentile": percentiles[2],
        "interquartile_range": iqr
    }
    return stats_dict


# In[12]:


data = [10, 20, 30, 40, 50]
print(descriptive_statistics(data))

