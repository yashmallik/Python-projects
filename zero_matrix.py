def setZeroes(matrix: list[list[int]]):
    """
    Do not return anything, modify matrix in-place instead.
    """
    place_list = []
    for array in range(len(matrix)):
        for elem in range(len(matrix[array])):

            if matrix[array][elem] == 0:
                temp_array = [array, elem]
                place_list.append(temp_array)

    while place_list:
        position = place_list.pop()
        row = position[0]
        column = position[1]

        for i in range(len(matrix[row])):
            matrix[row][i] = 0

        for j in range(len(matrix)):
            matrix[j][column] = 0
    print(matrix)


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

setZeroes(matrix)
