## [Implementation of Log Softmax Function](https://www.deep-ml.com/problems/39) ![Easy](https://img.shields.io/badge/-Easy-brightgreen)

In machine learning and statistics, the softmax function is a generalization of the logistic function that converts a vector of scores into probabilities. The log-softmax function is the logarithm of the softmax function, and it is often used for numerical stability when computing the softmax of large numbers.

Given a 1D numpy array of scores, implement a Python function to compute the log-softmax of the array.

### Example:

**Input:**

```
A = np.array([1, 2, 3])
print(log_softmax(A))
```


**Output:**

```array([-2.4076, -1.4076, -0.4076])```
