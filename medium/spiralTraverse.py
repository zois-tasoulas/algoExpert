def check_borders(borders):
    return borders[0] > borders[1] or borders[2] > borders[3]


def move_right(array, traversed_elements, borders):
    for index in range(borders[2], borders[3] + 1):
        traversed_elements.append(array[borders[0]][index])
    borders[0] += 1


def move_left(array, traversed_elements, borders):
    for index in range(borders[3], borders[2] - 1, -1):
        traversed_elements.append(array[borders[1]][index])
    borders[1] -= 1


def move_up(array, traversed_elements, borders):
    for index in range(borders[1], borders[0] - 1, -1):
        traversed_elements.append(array[index][borders[2]])
    borders[2] += 1


def move_down(array, traversed_elements, borders):
    for index in range(borders[0], borders[1] + 1):
        traversed_elements.append(array[index][borders[3]])
    borders[3] -= 1


def spiral_traverse(array):
    traversed_elements = []
    if array is not None:
        """
        borders[0], top border
        borders[1], bottom border
        borders[2], left border
        borders[3], right border
        """
        borders = [0, len(array) - 1, 0, len(array[0]) - 1]

        while True:
            move_right(array, traversed_elements, borders)
            if check_borders(borders):
                break
            move_down(array, traversed_elements, borders)
            if check_borders(borders):
                break
            move_left(array, traversed_elements, borders)
            if check_borders(borders):
                break
            move_up(array, traversed_elements, borders)
            if check_borders(borders):
                break

    return traversed_elements


def main():
    input_array = [
        [1, 2, 3, 4],
        [10, 11, 12, 5],
        [9, 8, 7, 6],
    ]
    print(spiral_traverse(input_array))


if __name__ == "__main__":
    main()
