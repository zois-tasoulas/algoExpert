def number_of_ways_to_traverse_graph(height, width):
    grid = [[1 for _ in range(width)] for _ in range(height)]

    for row in range(1, height):
        for column in range(1, width):
            grid[row][column] = grid[row - 1][column] + grid[row][column - 1]

    return grid[height - 1][width - 1]


def main():
    print(number_of_ways_to_traverse_graph(20, 1))
    print(number_of_ways_to_traverse_graph(1, 15))
    print(number_of_ways_to_traverse_graph(6, 10))


if __name__ == "__main__":
    main()
