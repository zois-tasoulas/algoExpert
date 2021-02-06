def search_in_sorted_matrix(matrix, target):
    if not matrix:
        raise Exception("Empty matrix provided")
    for row in matrix:
        if not row:
            raise Exception("Matrix contains empty row")
    rows = len(matrix)
    columns = len(matrix[0])

    if rows < columns:
        for row_index, row in enumerate(matrix):
            (found, column_index) = binary_search_row(row, 0, columns - 1, target)
            if found:
                return [row_index, column_index]
    else:
        for column_index in range(columns):
            (found, indices) = binary_search_column(
                matrix, column_index, 0, rows - 1, target
            )
            if found:
                return indices

    return [-1, -1]


def binary_search_row(array, l_index, r_index, target):
    while l_index <= r_index:
        median_index = (r_index + l_index) // 2
        median = array[median_index]
        if median == target:
            return (True, median_index)
        elif median < target:
            l_index = median_index + 1
        else:
            r_index = median_index - 1

    return (False, -1)


def binary_search_column(matrix, column_index, l_index, r_index, target):
    while l_index <= r_index:
        median_index = (r_index + l_index) // 2
        median = matrix[median_index][column_index]
        if median == target:
            return (True, [median_index, column_index])
        elif median < target:
            l_index = median_index + 1
        else:
            r_index = median_index - 1

    return (False, [-1, -1])


def search_in_sorted_matrix_b(matrix, target):
    row = len(matrix) - 1
    column = 0

    while row >= 0 and column < len(matrix[0]):
        if matrix[row][column] == target:
            return [row, column]
        elif matrix[row][column] > target:
            row -= 1
        else:
            column += 1

    return [-1, -1]


def main():
    matrix = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 4, 5, 6],
        [4, 5, 6, 7],
        [5, 6, 7, 8],
        [6, 7, 8, 9],
    ]
    print(search_in_sorted_matrix_b(matrix, 9))
    print(search_in_sorted_matrix_b(matrix, 10))


if __name__ == "__main__":
    main()
