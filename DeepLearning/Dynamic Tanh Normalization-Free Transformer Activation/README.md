## [Dynamic Tanh Normalization-Free Transformer Activation](https://www.deep-ml.com/problems/128) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Implement the Dynamic Tanh (DyT) function, a normalization-free transformation inspired by the Tanh function. DyT replaces layer normalization in Transformer architectures while preserving squashing behavior and enabling stable training.

### Example:

**Input:**

```python
x = np.array([[[0.14115588, 0.00372817, 0.24126647, 0.22183601]]])
gamma = np.ones((4,))
beta = np.zeros((4,))
alpha = 0.5
print(dynamic_tanh(x, alpha, gamma, beta))
```


**Output:**

```[[[0.0705, 0.0019, 0.1201, 0.1105]]]```
