

my_matrix = [[1,2,3], [4,5,6]]


def trans(matrix: list()) -> list():
    return list(zip(*matrix))


print(trans(my_matrix))