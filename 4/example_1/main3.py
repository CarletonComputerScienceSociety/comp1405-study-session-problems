lhs = [[1, 2, 3], [4, 5, 6]]
rhs = 5


def apply_scalar_to_maxtrix(matrix, scalar):
    lhs_rows, lhs_cols = len(matrix), len(matrix[0])

    result_matrix = []
    for row in range(lhs_rows):

        result_row = []

        for val in lhs[row]:
            result_row.append(val * scalar)

        result_matrix.append(result_row)

    return result_matrix


print(lhs)

print(apply_scalar_to_maxtrix(lhs, 2))
print(apply_scalar_to_maxtrix(lhs, 3))
print(apply_scalar_to_maxtrix(lhs, 100))
