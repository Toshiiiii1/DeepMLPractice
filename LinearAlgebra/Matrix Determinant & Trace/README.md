## [Matrix Determinant & Trace](https://www.deep-ml.com/problems/195) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Implement a function that computes both the determinant and trace of a square matrix. The determinant is a scalar value that can be computed from the elements of a square matrix and encodes certain properties of the matrix. The trace is simply the sum of the elements on the main diagonal. Return both values as a tuple.

### Example:

**Input:**

```python
matrix=[[2, 3], [1, 4]]
```


**Output:**

```(5.0, 6.0)```

## Solution:

- Đầu tiên bước tính trace thì dễ, chỉ cần tính tổng các phần tử trên đường chéo là xong.

- Tính định thức thì phải nhờ code mẫu.

- Dùng một hàng duy nhất để tính định thức thay vì toàn bộ hàng trong ma trận, đó là lí do vì sao code mẫu lại bỏ hàng đầu tiên đi.

- Dùng hàng i = 0 để tính định thức. Ma trận M sẽ bỏ đi hàng 0 và cột j.

## References

1. [Program to find Determinant of a Matrix](https://www.geeksforgeeks.org/dsa/determinant-of-a-matrix/)