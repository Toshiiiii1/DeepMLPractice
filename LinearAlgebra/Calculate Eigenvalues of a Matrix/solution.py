import math

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    # calculate trace = a + d
    trace = matrix[0][0] + matrix[-1][-1]
    # calculate determinant = ad - bc
    det = matrix[0][0] * matrix[-1][-1] - matrix[0][-1] * matrix[-1][0]

    # solve a quadratic equation to find eigenvalues
    delta = trace ** 2 - 4 * det
    if delta == 0:
        return [trace/2, trace/2]
    elif delta > 0:
        return sorted([(trace + math.sqrt(delta))/(2), (trace - math.sqrt(delta))/(2)], reverse=True)

matrix = [[2, 1], [1, 2]]
print(calculate_eigenvalues(matrix))

