def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Example: Transpose a matrix
original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed_matrix = transpose_matrix(original_matrix)
print("Original Matrix:", original_matrix)
print("Transposed Matrix:", transposed_matrix)
