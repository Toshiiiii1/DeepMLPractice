## [Implement Compressed Row Sparse Matrix (CSR) Format Conversion](https://www.deep-ml.com/problems/65) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Your task is to implement a function that converts a given dense matrix into the Compressed Row Sparse (CSR) format, an efficient storage representation for sparse matrices. The CSR format only stores non-zero elements and their positions, significantly reducing memory usage for matrices with a large number of zeros.

Write a function `compressed_row_sparse_matrix(dense_matrix)` that takes a 2D list `dense_matrix` as input and returns a tuple containing three lists:

- Values array: List of all non-zero elements in row-major order.
- Column indices array: Column index for each non-zero element in the values array.
- Row pointer array: Cumulative number of non-zero elements per row, indicating the start of each row in the values array.

### Example:

**Input:**

```python
dense_matrix = [
    [1, 0, 0, 0],
    [0, 2, 0, 0],
    [3, 0, 4, 0],
    [1, 0, 0, 5]
]

vals, col_idx, row_ptr = compressed_row_sparse_matrix(dense_matrix)
print("Values array:", vals)
print("Column indices array:", col_idx)
print("Row pointer array:", row_ptr)
```


**Output:**

```
Values array: [1, 2, 3, 4, 1, 5]
Column indices array: [0, 1, 0, 2, 0, 3]
Row pointer array: [0, 1, 2, 4, 6]
```
### Note:
Row pointer array is used to find the start index of the row contain non-zero values in the original matrix.

For example:
- (0, 1) implies 1 in the value array, which mean the first row in original matrix contain only one non-zero value is 1.
- (1, 2) implies 2 in the value array, which mean the second row in original matrix contain only one non-zero value is 2.
- (2, 3) implies 3 and 4 in the value array, which mean the third row in original matrix contain two non-zero values are 3 and 4.
- ...