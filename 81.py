def min_sum(matrix):
    # Dynamic programming:  value of result[m,n] is the value of matrix[m,n] plus the max of result[m, n-1] and result[m-1, n]
    dimensions = len(matrix)
    result = [[None] * dimensions] * dimensions
    for row_number in range(dimensions):
        for column_number in range(dimensions):
            if row_number == 0 and column_number == 0:
                result[0][0] = matrix[0][0]
            elif row_number == 0:
                result[row_number][column_number] = matrix[row_number][column_number] + result[row_number][column_number - 1]
            elif column_number == 0:
                result[row_number][column_number] = matrix[row_number][column_number] + result[row_number - 1][column_number]
            else:
                result[row_number][column_number] = min(matrix[row_number][column_number] + result[row_number - 1][column_number], matrix[row_number][column_number] + result[row_number][column_number - 1])
    return result[dimensions - 1][dimensions -1]

test_matrix = [[131, 673, 234, 103, 18], [201, 96, 342, 965, 150], [630, 803, 746, 422, 111], [537, 699, 497, 121, 956], [805, 732, 524, 37, 331]]

# Put in the input matrix string
input_matrix = input_matrix.split("\n")
for i in range(len(input_matrix)):
    input_matrix[i] = input_matrix[i].split(',')
    for j in range(len(input_matrix[i])):
            input_matrix[i][j] = int(input_matrix[i][j])

min_sum(input_matrix)
