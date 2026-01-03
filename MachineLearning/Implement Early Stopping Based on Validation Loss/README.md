## [Implement Early Stopping Based on Validation Loss](https://www.deep-ml.com/problems/135) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Create a function to decide when to stop training a model early based on a list of validation losses. The early stopping criterion should stop training if the validation loss hasn't improved for a specified number of epochs (patience), and only count as improvement if the loss decreases by more than a certain threshold (min_delta). Your function should return the epoch to stop at and the best epoch that achieved the lowest validation loss.

### Example:

**Input:**

```python
[0.9, 0.8, 0.75, 0.77, 0.76, 0.77, 0.78]
patience=2
min_delta=0.01
```


**Output:**

```(4, 2)```
