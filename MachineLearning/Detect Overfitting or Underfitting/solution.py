#!/usr/bin/env python
# coding: utf-8

# In[3]:


def model_fit_quality(training_accuracy, test_accuracy):
    if training_accuracy - test_accuracy > 0.2:
        return "1"
    elif training_accuracy < 0.7 and test_accuracy < 0.7:
        return "-1"
    else:
        return 0


# In[4]:


training_accuracy = 0.95
test_accuracy = 0.65
print(model_fit_quality(training_accuracy, test_accuracy))

