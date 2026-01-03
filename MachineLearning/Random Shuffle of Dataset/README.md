## [Random Shuffle of Dataset](https://www.deep-ml.com/problems/29) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Write a Python function to perform a random shuffle of the samples in two numpy arrays, X and y, while maintaining the corresponding order between them. The function should have an optional seed parameter for reproducibility.

### Example:

**Input:**

```
X = np.array([[1, 2], 
                  [3, 4], 
                  [5, 6], 
                  [7, 8]])
y = np.array([1, 2, 3, 4])
seed=42
```


**Output:**

```
(array([[3, 4], [7, 8], [1, 2], [5, 6]]), array([2, 4, 1, 3]))
```
