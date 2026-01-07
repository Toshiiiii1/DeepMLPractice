def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    columns = new_shape[1]
    if len(a) + len(a[0]) == sum(new_shape):
        newArray = []
        for row in a:
            for i in range(0, len(row), columns):
                newArray.append(row[i:i+columns])

        return newArray
    else:
        return []

a = [[1,2,3,4],[5,6,7,8]]
new_shape = (4, 2)
print(reshape_matrix(a, new_shape))

