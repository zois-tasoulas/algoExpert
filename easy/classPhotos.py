def class_photos(red_group, blue_group):
    red_group.sort()
    blue_group.sort()
    red, blue = 0, 1

    if red_group[0] == blue_group[0]:
        return False
    elif red_group[0] > blue_group[0]:
        front_row = blue
    else:
        front_row = red

    for index in range(1, len(red_group)):
        if front_row == blue:
            if red_group[index] <= blue_group[index]:
                return False
        else:
            if blue_group[index] <= red_group[index]:
                return False

    return True


def main():
    red_group = [5, 1, 4, 5, 6, 7, 8, 9]
    blue_group = [3, 4, 5, 6, 10, 7, 8, 9]
    print(class_photos(red_group, blue_group))


if __name__ == "__main__":
    main()
