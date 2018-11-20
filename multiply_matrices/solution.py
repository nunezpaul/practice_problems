class Matrix(object):
    def __init__(self, matrix):
        assert self._matching_width(matrix)
        self.height = len(matrix)
        self.width = len(matrix[0])
        self.matrix = matrix

    def _matching_width(self, matrix):
        check = True
        for idx, row in enumerate(matrix):
            if idx == 0:
                prev_len = len(row)
                continue

            check &= prev_len == len(row)
        return check

    def mat_mul(self, matrix2):
        result = self._init_resulting_matrix(matrix2)
        for matrix2_x in range(matrix2.width):
            for matrix1_y in range(self.height):
                sum = 0
                for matrix1_x in range(self.width):
                    sum += self.get_val(matrix1_x, matrix1_y) * matrix2.get_val(matrix2_x, matrix1_x)
                result.insert_val(matrix2_x, matrix1_y, sum)

        return result

    def _init_resulting_matrix(self, m2):
        col = [] * self.height
        for _ in range(m2.width):
            col.append([0] * m2.width)
        result = Matrix(col)
        return result

    def get_val(self, x, y):
        return self.matrix[y][x]

    def insert_val(self, x, y, val):
        self.matrix[y][x] = val


def matrix_multiply(matrix_1, matrix_2):
    class_matrix_1 = Matrix(matrix_1)
    return class_matrix_1.mat_mul(Matrix(matrix_2))


if __name__ == '__main__':
    matrix_1 = [[1, 2, 3], [4, 5, 6]]
    matrix_2 = [[7, 8], [9, 10], [11, 12]]
    result = matrix_multiply(matrix_1, matrix_2)
    for row in result.matrix:
        print(row)
