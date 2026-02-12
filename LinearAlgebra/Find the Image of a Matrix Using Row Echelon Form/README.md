## [Find the Image of a Matrix Using Row Echelon Form](https://www.deep-ml.com/problems/68) ![Difficulty](https://img.shields.io/badge/-Medium-yellow)

In this task, you are required to implement a function matrix_image(A) that calculates the column space of a given matrix A. The column space, also known as the image or span, consists of all linear combinations of the columns of A. To find this, you'll use concepts from linear algebra, focusing on identifying independent columns that span the matrix's image. Your task: Implement the function matrix_image(A) to return the basis vectors that span the column space of A. These vectors should be extracted from the original matrix and correspond to the independent columns.

### Example:

**Input:**

```python
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(matrix_image(matrix))
```


**Output:**

```
[[1, 2],
 [4, 5],
 [7, 8]]
```

## Solution:

- Đầu tiên, sử dụng thuật toán Khử Gauss-Jordan để đưa ma trận về dạng Row Echelon Form (REF). Chỉ cần dạng REF là đủ cho bài này.

- Sau khi có ma trận RREF, hãy quan sát xem số khác 0 đầu tiên của mỗi hàng nằm ở cột nào.

- Quay lại ma trận ban đầu và chọn ra các cột tương ứng với vị trí các cột Pivot đã tìm thấy.