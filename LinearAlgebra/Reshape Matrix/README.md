## [Reshape Matrix](https://www.deep-ml.com/problems/3) ![Easy](https://img.shields.io/badge/-Easy-brightgreen)

Write a Python function that reshapes a given matrix into a specified shape. if it cant be reshaped return back an empty list [ ].

### Example:

**Input:**

```a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)```


**Output:**

```[[1, 2], [3, 4], [5, 6], [7, 8]]```

### Solution:

Đề bài cho ma trận a và shape mới của ma trận, ở cái shape mới chỉ cần chú ý giá trị columns là ok.

Duyệt qua từng row trong ma trận a, dùng một loop (i=0, i < len(row), i += columns), mỗi row thì dùng slicing từ khoảng i -> i + columns tạo thành row mới, thêm row mới vào ma trận kết quả là xong.