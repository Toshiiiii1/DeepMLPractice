## [Compute Multi-class Cross-Entropy Loss](https://www.deep-ml.com/problems/134) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Implement a function that computes the average cross-entropy loss for a batch of predictions in a multi-class classification task. Your function should take in a batch of predicted probabilities and one-hot encoded true labels, then return the average cross-entropy loss. Ensure that you handle numerical stability by clipping probabilities by epsilon.

### Example:

**Input:**

```python
predicted_probs = [[0.7, 0.2, 0.1], [0.3, 0.6, 0.1]]
true_labels = [[1, 0, 0], [0, 1, 0]]
```


**Output:**

```0.4338```
