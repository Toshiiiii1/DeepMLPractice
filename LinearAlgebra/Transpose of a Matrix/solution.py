def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    # a = [[a00, a01, a02,... a0n], [a10, a11, a12,... a1n]]
    # zip(*a) = (a00, a10), (a01, a11), (a02, a12),... (a0n, a1n)
    # map(): (a00, a10) -> [a00, a10]
    return list(map(list, zip(*a)))

a = [[1,2,3],[4,5,6]]
print(transpose_matrix(a))

