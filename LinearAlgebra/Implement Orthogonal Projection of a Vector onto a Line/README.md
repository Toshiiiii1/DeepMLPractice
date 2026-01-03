## [Implement Orthogonal Projection of a Vector onto a Line](https://www.deep-ml.com/problems/66) ![Difficulty](https://img.shields.io/badge/-Easy-brightgreen)

Your task is to implement a function that calculates the orthogonal projection of a vector v onto another vector L. This projection results in the vector on L that is closest to v.

Write a function `orthogonal_projection(v, L)` that takes in two lists, `v` (the vector to be projected) and `L` (the line vector), and returns the orthogonal projection of `v` onto `L`. The function should output a list representing the projection vector rounded to three decimal places.

### Example:

**Input:**

```python
v = [3, 4]
L = [1, 0]
print(orthogonal_projection(v, L))
```


**Output:**

```[3.0, 0.0]```
