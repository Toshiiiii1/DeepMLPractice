## [Implement a Simple Residual Block with Shortcut Connection](https://www.deep-ml.com/problems/113) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Implement a function that creates a simple residual block using NumPy. The block should take a 1D input array, process it through two weight layers (using matrix multiplication), apply ReLU activations, and add the original input via a shortcut connection before a final ReLU activation.

### Example:

**Input:**

```python
x = np.array([1.0, 2.0])
w1 = np.array([[1.0, 0.0], [0.0, 1.0]])
w2 = np.array([[0.5, 0.0], [0.0, 0.5]])
```


**Output:**

```[1.5, 3.0]```
