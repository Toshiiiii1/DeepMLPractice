## [Singular Value Decomposition (SVD) of 2x2 Matrix](https://www.deep-ml.com/problems/12) ![Difficulty](https://img.shields.io/badge/-Hard-red)

Write a Python function that computes an approximate Singular Value Decomposition (SVD) of a real 2x2 matrix using one Jacobi rotation.

Input:

- ```A```: a NumPy array of shape (2, 2)

Rules:

- You may use basic NumPy operations (matrix multiplication, transpose, element-wise math, etc.)

- Do NOT call numpy.linalg.svd or any other high-level SVD routine

- Use a single Jacobi rotation step (no iterative refinements)

Return: A tuple ```(U, S, Vt)``` where:

- ```U``` is a 2x2 orthogonal matrix (left singular vectors)

- ```S``` is a length-2 NumPy array containing the singular values

- ```Vt``` is the transpose of the right singular vector matrix V

The decomposition should approximately satisfy: ```A = U @ diag(S) @ Vt```

### Example:

**Input:**

```python
A = np.array([[2, 1], [1, 2]])
```


**Output:**

```
U ≈ [[0.707, -0.707], [0.707, 0.707]]
S = [3.0, 1.0]
Vt ≈ [[0.707, 0.707], [-0.707, 0.707]]
```

## Solution:

[![](https://mermaid.ink/img/pako:eNp1Uz9v00AU_ypPNyWV09iOmzQWLW0SkEACoSRdsC10ta-21fgcrucoIYpU1AWJhY4wUXWoGCpYkJAzMKTqSD-D-SSc7QQcBJZsvTu_35_37t0U2aFDkI5choce9DsmBfH0OGa8ZLSS-DOHm_Mkvop0eOol8TWFAANnWbQP6li1ylCp7EI7pCPC-MNBiLnR9qJJMj9LM04wdeHYF6sIjtKfVq5QzF8SBMOIk5bRX1xTr6Ai5OfnPoyT-SdB1YId2E--nsIe7C-pVoQ5PifziH384GWEB1MTtQxZki3Y2YGWoUiKdd9EszXk72SBhZt3i1jopCx9j3D8zNeMH9-E6t1pVbP-hehh_096Gw9sw0QZQqmqsAGY2RzTkrqR-lAsqEJp6aiyNFQum2itlpVwXgsjmJOu0U_ii7DQl3GIJ_AY2-GhD12rAEwtFJFrteZbxY73fDfAwnLe947w3c372xJvF-4dsuou3J2J_Z9vPjg-dkudv_0WmTLqXsi40RPTMxTnFn8fpnjXT-LLABwxTBRGi485sxcuLsQymb8FO5m_5-n3Cgtdfvvl9kIcRHbsa2opeabyiI5y83-PDHU9QWh72ehehuDT0YuTNHONZwUvNuNgyXWQjllW_95_0CtAhu4SHjFaMvpC_zKt5rUOB5KoWsqaaZWRhALCAuw74q5NUwYTcY8ExES6CB3Mjk1k0pnIwxEPexNqI52ziEgoGjriyDqi8QwHq03i-DxkT_K7m11hCQ0xRfoUjZGuatqmpqhasy7XtpSGCCU0QXqlpjU3m7KsbcsNTZOVZr0-k9CrMBS0yuZ2Y6uuyVu1WrPRUBvbioRYGLke0o_w4IRk9M-z1NyBy9Ja8pgR6hDWDiPKkV5T1dkvhQV-BQ?type=png)](https://mermaid.live/edit#pako:eNp1Uz9v00AU_ypPNyWV09iOmzQWLW0SkEACoSRdsC10ta-21fgcrucoIYpU1AWJhY4wUXWoGCpYkJAzMKTqSD-D-SSc7QQcBJZsvTu_35_37t0U2aFDkI5choce9DsmBfH0OGa8ZLSS-DOHm_Mkvop0eOol8TWFAANnWbQP6li1ylCp7EI7pCPC-MNBiLnR9qJJMj9LM04wdeHYF6sIjtKfVq5QzF8SBMOIk5bRX1xTr6Ai5OfnPoyT-SdB1YId2E--nsIe7C-pVoQ5PifziH384GWEB1MTtQxZki3Y2YGWoUiKdd9EszXk72SBhZt3i1jopCx9j3D8zNeMH9-E6t1pVbP-hehh_096Gw9sw0QZQqmqsAGY2RzTkrqR-lAsqEJp6aiyNFQum2itlpVwXgsjmJOu0U_ii7DQl3GIJ_AY2-GhD12rAEwtFJFrteZbxY73fDfAwnLe947w3c372xJvF-4dsuou3J2J_Z9vPjg-dkudv_0WmTLqXsi40RPTMxTnFn8fpnjXT-LLABwxTBRGi485sxcuLsQymb8FO5m_5-n3Cgtdfvvl9kIcRHbsa2opeabyiI5y83-PDHU9QWh72ehehuDT0YuTNHONZwUvNuNgyXWQjllW_95_0CtAhu4SHjFaMvpC_zKt5rUOB5KoWsqaaZWRhALCAuw74q5NUwYTcY8ExES6CB3Mjk1k0pnIwxEPexNqI52ziEgoGjriyDqi8QwHq03i-DxkT_K7m11hCQ0xRfoUjZGuatqmpqhasy7XtpSGCCU0QXqlpjU3m7KsbcsNTZOVZr0-k9CrMBS0yuZ2Y6uuyVu1WrPRUBvbioRYGLke0o_w4IRk9M-z1NyBy9Ja8pgR6hDWDiPKkV5T1dkvhQV-BQ)

## References:

[1] []()