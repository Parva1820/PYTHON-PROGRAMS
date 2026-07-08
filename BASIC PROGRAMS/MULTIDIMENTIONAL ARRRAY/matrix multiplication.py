A = [[1, 2, 3, 4],
     [1, 2, 3, 4],
     [1, 2, 3, 4]]

B = [[5, 6, 7],
     [5, 6, 7],
     [5, 6, 7],
     [5, 6, 7]]


def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B
                result[i][j] += A[i][k] * B[k][j]
    return result


result = matrix_multiply(A, B)
print(result)
