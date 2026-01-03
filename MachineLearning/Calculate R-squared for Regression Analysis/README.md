## [Calculate R-squared for Regression Analysis](https://www.deep-ml.com/problems/69) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

R-squared, also known as the coefficient of determination, is a measure that indicates how well the independent variables explain the variability of the dependent variable in a regression model.

Your Task: To implement the function `r_squared(y_true, y_pred)` that calculates the R-squared value, given arrays of true values `y_true` and predicted values `y_pred`.

### Example:

**Input:**

```python
import numpy as np

y_true = np.array([1, 2, 3, 4, 5])
y_pred = np.array([1.1, 2.1, 2.9, 4.2, 4.8])
print(r_squared(y_true, y_pred))
```


**Output:**

```0.989```
