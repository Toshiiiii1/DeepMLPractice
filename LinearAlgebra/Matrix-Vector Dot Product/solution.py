def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    # check if the number of columns in a equals the length of vector b
    if len(a[0]) != len(b):
        return -1

    '''
    - sum(x * y for x, y in zip(row, b)): calculates the dot product of each row in matrix a with vector b.
    - [ ... for row in a]: iterates through each row of matrix a.
    '''
    return [sum(x * y for x, y in zip(row, b)) for row in a]

# input
a = [[1, 2], [2, 4]]
b = [1, 2]
print(matrix_dot_vector(a, b))