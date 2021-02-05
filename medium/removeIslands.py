def mark_border_water(area, row, column, height, width):
    if area[row][column] == 1:
        area[row][column] = 2
        if row > 0:
            mark_border_water(area, row - 1, column, height, width)
        if row < height - 1:
            mark_border_water(area, row + 1, column, height, width)
        if column > 0:
            mark_border_water(area, row, column - 1, height, width)
        if column < width - 1:
            mark_border_water(area, row, column + 1, height, width)


def remove_islands(area):
    if area is None:
        raise Exception("Empty map given")

    for row in area:
        if row is None:
            raise Exception("Empty row found")

    height = len(area)
    width = len(area[0])

    # Modify costal water, startinf on top and bottom
    for row in [0, height - 1]:
        for column in range(width):
            if area[row][column] == 1:
                mark_border_water(area, row, column, height, width)

    # Modify costal water, starting left and right
    for column in [0, width - 1]:
        for row in range(height):
            if area[row][column] == 1:
                mark_border_water(area, row, column, height, width)

    # Remove islands and restore costal water
    for row in range(height):
        for column in range(width):
            if area[row][column] == 1:
                area[row][column] = 0
            elif area[row][column] == 2:
                area[row][column] = 1

    return area


def main():
    height = 5
    width = 7
    area = [[] for _ in range(height)]
    area[0] = [0, 0, 0, 0, 1, 1, 0]
    area[1] = [0, 0, 0, 0, 0, 0, 0]
    area[2] = [0, 0, 0, 1, 1, 0, 0]
    area[3] = [1, 1, 0, 1, 0, 1, 0]
    area[4] = [1, 1, 0, 0, 0, 0, 0]

    remove_islands(area)

    for line in area:
        print(line)


if __name__ == "__main__":
    main()
