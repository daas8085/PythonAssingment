def add_matrices(matrix1, matrix2):
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    return result

# Example: Add two matrices
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
result_matrix = add_matrices(matrix_a, matrix_b)
print("Resultant Matrix:", result_matrix)
