import numpy as np

def gaussian_elimination(A, b):
    """
    Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
    :param A: Coefficient matrix
    :param b: Right-hand side vector
    :return: Solution vector x
    """


    h = 0
    k = 0
    m, n = A.shape
    epsilon = 1e-10  # ngưỡng xác định "bằng 0"

    while h < m and k < n:
        # 1. Tìm pivot (chỉ từ hàng h trở xuống)
        i_max = h + np.argmax(np.abs(A[h:, k]))
        
        # 2. Kiểm tra pivot có ≈ 0 không
        if np.abs(A[i_max, k]) < epsilon:
            # Cột này toàn 0, bỏ qua, chuyển sang cột kế
            k += 1
            continue
        
        # 3. Hoán đổi hàng nếu cần
        if i_max != h:
            A[[h, i_max]] = A[[i_max, h]]
            b[[h, i_max]] = b[[i_max, h]]
        
        # 4. Khử Gauss cho các hàng dưới
        for i in range(h+1, m):
            factor = A[i, k] / A[h, k]
            A[i, k] = 0  # có thể bỏ qua, tự hiểu
            
            # Cập nhật các cột từ k+1 đến n-1
            A[i, k+1:] -= factor * A[h, k+1:]
            b[i] -= factor * b[h]
        
        h += 1
        k += 1

    # Backwards Substitution
    x = [1 for _ in range(m)]
    for i in range(m-1, -1, -1):
        summ = 0
        # Thế nghiệm các x đã tìm được trước đó vào p.trình phía trên để tính nghiệm x còn lại
        for j in range(i+1, m):
            summ += A[i, j] * x[j]
        if A[i, i] != 0:
            # Tính nghiệm x ở hàng cuối cùng dần lên hàng đầu tiên
            x[i] = (b[i] - summ) / A[i][i]

        else:
            if b[i] - summ == 0:
                x[i] = 0
    return x


A = np.array([[2,8,4], [2,5,1], [4,10,-1]], dtype=float)
b = np.array([2,5,1], dtype=float)

