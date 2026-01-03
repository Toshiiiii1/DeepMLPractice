## [Batch Iterator for Dataset](https://www.deep-ml.com/problems/30) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Implement a batch iterable function that samples in a numpy array X and an optional numpy array y. The function should yield batches of a specified size. If y is provided, the function should yield batches of (X, y) pairs; otherwise, it should yield batches of X only.

### Example:

**Input:**

```
X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8], 
                  [9, 10]])
y = np.array([1, 2, 3, 4, 5])
batch_size = 2
```


**Output:**

```
[[[[1, 2], [3, 4]], [1, 2]],
     [[[5, 6], [7, 8]], [3, 4]],
     [[[9, 10]], [5]]]
```
