def first_duplicate_value(array):
    dictionary = dict()
    for index in range(1, len(array) + 1):
        dictionary[index] = False

    for element in array:
        if dictionary[element]:
            return element
        dictionary[element] = True

    return -1


def main():
    array = [5, 3, 6, 4, 2, 6, 8, 4]
    print(first_duplicate_value(array))


if __name__ == "__main__":
    main()
