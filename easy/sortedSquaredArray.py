def sorted_squared_array(array):
    non_negative = len(array)

    for index, _ in enumerate(array):
        if array[index] >= 0:
            non_negative = index
            break

    output = []
    negative = non_negative - 1
    while negative >= 0 and non_negative < len(array):
        if abs(array[negative]) < array[non_negative]:
            output.append(array[negative] ** 2)
            negative -= 1
        else:
            output.append(array[non_negative] ** 2)
            non_negative += 1

    for index in range(negative, -1, -1):
        output.append(array[index] ** 2)
    for index in range(non_negative, len(array)):
        output.append(array[index] ** 2)

    return output


def main():
    array = [-3, -1, 3, 4, 5, 6, 7, 8, 9]
    print(sorted_squared_array(array))


if __name__ == "__main__":
    main()
