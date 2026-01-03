## [Implement Batch Normalization for BCHW Input](https://www.deep-ml.com/problems/115) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Implement a function that performs Batch Normalization on a 4D NumPy array representing a batch of feature maps in the BCHW format (batch, channels, height, width). The function should normalize the input across the batch and spatial dimensions for each channel, then apply scale (gamma) and shift (beta) parameters. Use the provided epsilon value to ensure numerical stability.

### Example:

**Input:**

```python
B, C, H, W = 2, 2, 2, 2
np.random.seed(42)
X = np.random.randn(B, C, H, W)
gamma = np.ones(C).reshape(1, C, 1, 1)
beta = np.zeros(C).reshape(1, C, 1, 1)
```


**Output:**

```
[[[[ 0.42859934 -0.51776438]
   [ 0.65360963  1.95820707]]

  [[ 0.02353721  0.02355215]
   [ 1.67355207  0.93490043]]]


 [[[-1.01139563  0.49692747]
   [-1.00236882 -1.00581468]]

  [[ 0.45676349 -1.50433085]
   [-1.33293647 -0.27503802]]]]
```
