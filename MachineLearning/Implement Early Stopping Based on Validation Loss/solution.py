#!/usr/bin/env python
# coding: utf-8

# In[50]:


from typing import Tuple

def early_stopping(losses: list[float], patience: int, min_delta: float) -> Tuple[int, int]:
    best_loss = losses[0]
    best_loss_epoch = 0
    patience_counter = 0
    for current_epoch in range(1, len(losses)):
        if best_loss - losses[current_epoch] > min_delta:
            best_loss = losses[current_epoch]
            best_loss_epoch = current_epoch
            patience_counter = 0  # reset nếu có cải thiện
        else:
            patience_counter += 1
            if patience_counter == patience:
                break  # lúc này mới dừng

    return (current_epoch, best_loss_epoch)


# In[53]:


print(early_stopping([0.9, 0.8, 0.75, 0.77, 0.76, 0.77, 0.78], 2, 0.01))

