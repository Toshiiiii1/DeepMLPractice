## [source deep_ml_VM/Scripts/activate](https://www.deep-ml.com/problems/114) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Implement a function that performs Global Average Pooling on a 3D NumPy array representing feature maps from a convolutional layer. The function should take an input of shape (height, width, channels) and return a 1D array of shape (channels,), where each element is the average of all values in the corresponding feature map.

### Example:

**Input:**

```python
x = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
```


**Output:**

```[5.5, 6.5, 7.5]```
