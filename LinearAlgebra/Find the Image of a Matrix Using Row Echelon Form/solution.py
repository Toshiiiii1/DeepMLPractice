import numpy as np

def matrix_image(matrix):
    # Copy ma trận, ma trận gốc dùng để tham chiếu cuối hàm, ma trận copy dùng để biến đổi sang dạng REF
    copy_matrix = matrix.astype(float).copy()
    h = 0
    k = 0
    m, n = copy_matrix.shape
    epsilon = 1e-10
    pivots = []

    while (h < m and k < n):
        # 1. Tìm pivot (chỉ từ hàng h trở xuống)
        i_max = h + np.argmax(np.abs(copy_matrix[h:, k]))

        # 2. Kiểm tra pivot có ≈ 0 không
        if np.abs(copy_matrix[i_max, k]) < epsilon:
            # Cột này toàn 0, bỏ qua, chuyển sang cột kế
            k += 1
            continue

        # Cột k hiện tại là cột chắc chắn chứa pivot nên thêm vị trí k vào danh sách pivot
        pivots.append(k)
        # 3. Hoán đổi hàng nếu cần
        if (i_max != h):
            copy_matrix[[h, i_max]] = copy_matrix[[i_max, h]]

        # 4. Khử Gauss cho các hàng dưới
        for i in range(h+1, m):
            factor = copy_matrix[i, k] / copy_matrix[h, k]
            copy_matrix[i, k] = 0

            # Cập nhật các cột từ k+1 đến n-1
            copy_matrix[i, k+1:] -= factor * copy_matrix[h, k+1:]

        h += 1
        k += 1

    return matrix[:, pivots]

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=float)

print(matrix_image(matrix))