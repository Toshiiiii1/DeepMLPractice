#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculate_brightness(img):
    # Check for None or empty image
    if not img or not img[0]:
        return -1

    # Get dimensions and validate row consistency
    rows, cols = len(img), len(img[0])
    if any(len(row) != cols for row in img):
        return -1

    # Calculate sum and validate pixel values
    total = 0
    for row in img:
        for pixel in row:
            if not 0 <= pixel <= 255:
                return -1
            total += pixel

    # Return average rounded to 2 decimal places
    return round(total / (rows * cols), 2)


# In[20]:


img = [
    [100, 200],
    [50, 150]
]
print(calculate_brightness(img))

