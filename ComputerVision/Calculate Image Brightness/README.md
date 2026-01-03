## [Calculate Image Brightness](https://www.deep-ml.com/problems/70) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

In this task, you will implement a function `calculate_brightness(img)` that calculates the average brightness of a grayscale image. The image is represented as a 2D matrix, where each element represents a pixel value between 0 (black) and 255 (white).

Your Task:
Implement the function calculate_brightness(img) to:

1. Return the average brightness of the image rounded to two decimal places.
2. Handle edge cases:
    - If the image matrix is empty.
    - If the rows in the matrix have inconsistent lengths.
    - If any pixel values are outside the valid range (0-255).

For any of these edge cases, the function should return -1.

### Example:

**Input:**

```python
img = [
    [100, 200],
    [50, 150]
]
print(calculate_brightness(img))
```


**Output:**

```125.0```
