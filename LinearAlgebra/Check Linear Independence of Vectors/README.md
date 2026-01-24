## [Check Linear Independence of Vectors](https://www.deep-ml.com/problems/331) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Implement a function to determine whether a given set of vectors is linearly independent.

A set of vectors is linearly independent if no vector in the set can be expressed as a linear combination of the others. Equivalently, the only way to get the zero vector from a linear combination of the vectors is if all the coefficients are zero.

Your function should take a list of vectors (where each vector is represented as a list of floats) and return True if the vectors are linearly independent, and False otherwise.

Note: An empty set of vectors is considered linearly independent by convention.

### Example:

**Input:**

```python
vectors = [[1, 2], [2, 4]]
```


**Output:**

```False```


## Solution:

- Dựa vào phần lý thuyết được cung cấp để giải.

- Giải phương trình tuyến tính không phải là ý hay. Thế thì nhờ vào cái hint trong phần lý thuyết.

- Rank của ma trận bằng với số lượng vector thì các vector là độc lập tuyến tính.