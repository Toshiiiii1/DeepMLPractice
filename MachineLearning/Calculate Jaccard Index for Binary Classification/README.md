## [Calculate Jaccard Index for Binary Classification](https://www.deep-ml.com/problems/72) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Your task is to implement a function `jaccard_index(y_true, y_pred)` that calculates the Jaccard Index, a measure of similarity between two binary sets. The Jaccard Index is widely used in binary classification tasks to evaluate the overlap between predicted and true labels.

Your Task:

Implement the function `jaccard_index(y_true, y_pred)` to:

1. Calculate the Jaccard Index between the arrays `y_true` and `y_pred`.
2. Return the Jaccard Index as a float value.
3. Ensure the function handles cases where:
    - There is no overlap between `y_true` and `y_pred`.
    - Both arrays contain only zeros (edge cases).

### Example:

**Input:**

```python
y_true = np.array([1, 0, 1, 1, 0, 1])
y_pred = np.array([1, 0, 1, 0, 0, 1])
print(jaccard_index(y_true, y_pred))
```


**Output:**

```0.75```
