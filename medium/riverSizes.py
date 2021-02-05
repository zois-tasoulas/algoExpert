def explore_river(area, row, column, height, width):
    # Check whether out of bounds or not on a river
    if (
        row < 0
        or column < 0
        or row > height - 1
        or column > width - 1
        or area[row][column] == 0
    ):
        return 0

    area[row][column] = 0
    return (
        1
        + explore_river(area, row - 1, column, height, width)
        + explore_river(area, row + 1, column, height, width)
        + explore_river(area, row, column - 1, height, width)
        + explore_river(area, row, column + 1, height, width)
    )


def river_sizes(area):
    if area is None or area[0] is None:
        raise Exception("Land map should not be empty")

    height = len(area)
    width = len(area[0])
    rivers = []
    for row in range(height):
        for column in range(width):
            if area[row][column] == 1:
                rivers.append(explore_river(area, row, column, height, width))

    return rivers


def main():
    height = 3
    width = 4
    area = [[] for x in range(height)]
    area[0] = [1, 0, 1, 0]
    area[1] = [1, 0, 1, 1]
    area[2] = [1, 0, 0, 0]

    print(river_sizes(area))


if __name__ == "__main__":
    main()
