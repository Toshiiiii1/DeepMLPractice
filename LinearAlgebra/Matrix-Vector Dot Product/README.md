## [Matrix-Vector Dot Product](https://www.deep-ml.com/problems/1) ![Easy](https://img.shields.io/badge/-Easy-brightgreen)

Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.

### Example:

**Input:**

```a = [[1, 2], [2, 4]], b = [1, 2]```


**Output:**

```[5, 10]```

### Solution:

Đầu tiên là kiểm tra số cột có bằng với số lượng phần tử của vector b hay không?

Lấy từng row trong ma trận, tính dot product giữa mỗi row với vector b.

Cách tính dot product cũ là dùng chỉ số index, cách mới là dùng hàm zip() để gộp những giá trị cùng chỉ số index thành một cặp.