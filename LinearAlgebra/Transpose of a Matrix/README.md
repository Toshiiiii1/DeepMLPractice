## [Transpose of a Matrix](https://www.deep-ml.com/problems/2) ![Easy](https://img.shields.io/badge/-Easy-brightgreen)

Write a Python function that computes the transpose of a given matrix.

### Example:

**Input:**

```a = [[1,2,3],[4,5,6]]```


**Output:**

```[[1,4],[2,5],[3,6]]```

### Solution:

Cách ban đầu là dùng 2 loop lồng nhau để lấy các phần tử mỗi cột, gom chúng vào một list (một row mới) rồi append vào ma trận mới.

Nhưng có cách hay hơn đó là dùng hàm zip(*a), *a dùng để tách từng row trong ma trận a thành từng tham số truyền vào hàm zip(). Phần còn lại của hàm zip() chỉ là gom các phần tử cùng vị trí ở từng row vào một tuple (một row mới). Biến đổi mỗi tuple thành list rồi tạo list mới gom các row mới là xong.