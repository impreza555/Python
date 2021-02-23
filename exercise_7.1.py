class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        result = []
        for i in zip(self.matrix, other.matrix):
            result.append([sum([j, k]) for j, k in zip(*i)])

        return Matrix(result)

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, i)) for i in self.matrix])


matrix_1 = [[5, 18, 11], [6, 17, 23], [41, 50, 9]]
matrix_2 = [[45, 8, 2], [6, 7, 93], [24, 5, 97]]

my_matrix_1 = Matrix(matrix_1)
my_matrix_2 = Matrix(matrix_2)

print(my_matrix_1)
print('-' * 10)
print(my_matrix_2)
print('-' * 10)
print(my_matrix_1 + my_matrix_2)
print('*' * 10, '\n')

matrix_1 = [[5, 18], [6, 17], [41, 50]]
matrix_2 = [[45, 8], [6, 7], [24, 5]]

my_matrix_1 = Matrix(matrix_1)
my_matrix_2 = Matrix(matrix_2)

print(my_matrix_1)
print('-' * 10)
print(my_matrix_2)
print('-' * 10)
print(my_matrix_1 + my_matrix_2)
print('*' * 10, '\n')

matrix_1 = [[5, 18, 11], [6, 17, 23]]
matrix_2 = [[45, 8, 2], [6, 7, 93]]

my_matrix_1 = Matrix(matrix_1)
my_matrix_2 = Matrix(matrix_2)

print(my_matrix_1)
print('-' * 10)
print(my_matrix_2)
print('-' * 10)
print(my_matrix_1 + my_matrix_2)
print('*' * 10, '\n')
