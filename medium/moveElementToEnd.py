def swap(index_1, index_2, array):
    temp = array[index_1]
    array[index_1] = array[index_2]
    array[index_2] = temp


def move_element_to_end(array, number):
    if array is None:
        raise Exception("Empty array passed to move_element_to_end")

    left_index = 0
    right_index = len(array) - 1

    while right_index >= 0 and array[right_index] == number:
        right_index -= 1

    while left_index < right_index:
        if array[left_index] == number:
            swap(left_index, right_index, array)
            while right_index >= 0 and array[right_index] == number:
                right_index -= 1

        left_index += 1

    return array


def main():
    array = [4, 5, 1, 12, 0, -23, 45, 6546, -2, 5, 0, 24, -18, 9]
    number = 5
    print(move_element_to_end(array, number))


if __name__ == "__main__":
    main()
