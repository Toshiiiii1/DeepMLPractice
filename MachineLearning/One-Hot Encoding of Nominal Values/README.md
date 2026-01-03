## [One-Hot Encoding of Nominal Values](https://www.deep-ml.com/problems/34) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Write a Python function to perform one-hot encoding of nominal values. The function should take in a 1D numpy array x of integer values and an optional integer n_col representing the number of columns for the one-hot encoded array. If n_col is not provided, it should be automatically determined from the input array.

### Example:

**Input:**

```x = np.array([0, 1, 2, 1, 0])```


**Output:**

```
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]
 [0. 1. 0.]
 [1. 0. 0.]]
```
