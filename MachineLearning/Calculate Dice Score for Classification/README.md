## [Calculate Dice Score for Classification](https://www.deep-ml.com/problems/73) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Your task is to implement a function `dice_score(y_true, y_pred)` that calculates the Dice Score, also known as the SÃ¸rensen-Dice coefficient or F1-score, for binary classification. The Dice Score is used to measure the similarity between two sets and is particularly useful in tasks like image segmentation and binary classification.

Implement the function dice_score(y_true, y_pred) to:

1. Calculate the Dice Score between the arrays y_true and y_pred.
2. Return the Dice Score as a float value rounded to 3 decimal places.
3. Handle edge cases appropriately, such as when there are no true or predicted positives.

### Example:

**Input:**

```python
y_true = np.array([1, 1, 0, 1, 0, 1])
y_pred = np.array([1, 1, 0, 0, 0, 1])
print(dice_score(y_true, y_pred))
```


**Output:**

```0.857```
