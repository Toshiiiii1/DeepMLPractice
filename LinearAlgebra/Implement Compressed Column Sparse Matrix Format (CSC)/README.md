## [Implement Compressed Column Sparse Matrix Format (CSC)](https://www.deep-ml.com/problems/67) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Your task is to implement a function that converts a dense matrix into its Compressed Column Sparse (CSC) representation. The CSC format stores only non-zero elements of the matrix and is efficient for matrices with a high number of zero elements.

Write a function `compressed_col_sparse_matrix(dense_matrix)` that takes in a two-dimensional list dense_matrix and returns a tuple of three lists:

- values: List of non-zero elements, stored in column-major order.
- row indices: List of row indices corresponding to each value in the values array.
- column pointer: List that indicates the starting index of each column in the values array.

### Example:

**Input:**

```python
dense_matrix = [
    [0, 0, 3, 0],
    [1, 0, 0, 4],
    [0, 2, 0, 0]
]

vals, row_idx, col_ptr = compressed_col_sparse_matrix(dense_matrix)
```


**Output:**

```[1, 2, 3, 4] [1, 2, 0, 1] [0, 1, 2, 3, 4]```
