## [Vector Norms (L1/L2/Frobenius)](https://www.deep-ml.com/problems/328) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Implement a function that computes different types of norms for vectors and matrices.

Vector norms are fundamental concepts in linear algebra that measure the "size" or "length" of vectors. Different norms have different properties and applications in machine learning, particularly in regularization and distance calculations.

Your Task: Write a function ```compute_norm(arr, norm_type)``` that takes:

- ```arr```: A numpy array (can be 1D or 2D)

- ```norm_type```: A string specifying which norm to compute ('l1', 'l2', or 'frobenius')

The function should return the computed norm as a float.

Constraints:

- For 'l1' and 'l2' norms, the input can be any array (1D or 2D)

- For 'frobenius' norm, the input is typically a 2D matrix

- All norms should treat the input as a flattened collection of elements when computing

### Example:

**Input:**

```python
arr = [3, -4], norm_type = 'l2'
```


**Output:**

```5.0```


## Solution:

- Áp dụng công thức ta có.