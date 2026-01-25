## [Gaussian Elimination for Solving Linear Systems](https://www.deep-ml.com/problems/58) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Your task is to implement the Gaussian Elimination method, which transforms a system of linear equations into an upper triangular matrix. This method can then be used to solve for the variables using backward substitution.

Write a function gaussian_elimination(A, b) that performs Gaussian Elimination with partial pivoting to solve the system (Ax = b).

The function should return the solution vector (x).

### Example:

**Input:**

```python
A = np.array([[2,8,4], [2,5,1], [4,10,-1]], dtype=float)
b = np.array([2,5,1], dtype=float)

print(gaussian_elimination(A, b))
```


**Output:**

```[11.0, -4.0, 3.0]```

## References

1. [Gaussian elimination](https://en-wikipedia-org.translate.goog/wiki/Gaussian_elimination?_x_tr_sl=en&_x_tr_tl=vi&_x_tr_hl=vi&_x_tr_pto=sge)