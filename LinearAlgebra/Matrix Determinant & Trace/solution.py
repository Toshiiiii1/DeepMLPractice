def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    det = determinant(matrix)
    trace = 0.0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    
    return (det, trace)

def determinant(matrix: list[list[float]]):
    n = len(matrix)
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    
    res = 0.0
    for col in range(n):
      
        # Create a submatrix by removing the first 
        # row and the current column
        sub = [[0] * (n - 1) for _ in range(n - 1)]
        for i in range(1, n):
            subcol = 0
            for j in range(n):
              
                # Skip the current column
                if j == col:
                    continue
                
                # Fill the submatrix
                sub[i - 1][subcol] = matrix[i][j]
                subcol += 1
        
        # Cofactor expansion
        sign = 1 if col % 2 == 0 else -1
        res += sign * matrix[0][col] * determinant(sub)
    
    return res

matrix = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]

print(matrix_determinant_and_trace(matrix))