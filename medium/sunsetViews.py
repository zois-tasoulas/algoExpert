def sunset_views(buildings, direction):
    if not buildings:
        return []

    index_with_view = []

    if direction == "WEST":
        tallest_prev = buildings[0]
        index_with_view.append(0)
        for index in range(1, len(buildings)):
            if buildings[index] > tallest_prev:
                tallest_prev = buildings[index]
                index_with_view.append(index)
    elif direction == "EAST":
        tallest_prev = buildings[-1]
        index_with_view.append(len(buildings) - 1)
        for index in range(len(buildings) - 2, -1, -1):
            if buildings[index] > tallest_prev:
                tallest_prev = buildings[index]
                index_with_view.append(index)

        index_with_view.reverse()

    else:
        raise Exception("Unexpected direction received")

    return index_with_view


def main():
    buildings = [1, 2, 3, 6, 4, 5, 3, 2, 2, 3, 1]
    direction = "EAST"
    print(sunset_views(buildings, direction))
    direction = "WEST"
    print(sunset_views(buildings, direction))


if __name__ == "__main__":
    main()
