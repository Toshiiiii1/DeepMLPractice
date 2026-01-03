## [Generate a Confusion Matrix for Binary Classification](https://www.deep-ml.com/problems/75) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Your task is to implement the function `confusion_matrix(data)` that generates a confusion matrix for a binary classification problem. The confusion matrix provides a summary of the prediction results on a classification problem, allowing you to visualize how many data points were correctly or incorrectly labeled.

Input:
- A list of lists, where each inner list represents a pair
- `[y_true, y_pred]` for one observation. `y_true` is the actual label, and `y_pred` is the predicted label.

Output:
- A 2×2 confusion matrix represented as a list of lists.

### Example:

**Input:**

```python
data = [[1, 1], [1, 0], [0, 1], [0, 0], [0, 1]]
print(confusion_matrix(data))
```


**Output:**

```[[1, 1], [2, 1]]```
