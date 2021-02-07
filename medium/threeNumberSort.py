def three_number_sort_a(array, order):
    last_a = -1
    last_b = -1
    for index, number in enumerate(array):
        if number == order[0]:
            last_a += 1
            swap(array, last_a, index)
            last_b += 1
            if last_b != last_a:
                swap(array, last_b, index)
        elif number == order[1]:
            if last_b == -1:
                last_b = last_a
            last_b += 1
            swap(array, last_b, index)
        elif number == order[2]:
            continue
        else:
            raise Exception("Number not appearing in order array")

    return array


def three_number_sort(array, order):
    after_a = 0
    before_c = len(array) - 1
    current = 0

    while current <= before_c and after_a < before_c:
        if array[current] == order[0]:
            swap(array, current, after_a)
            after_a += 1
            current += 1
        elif array[current] == order[2]:
            swap(array, current, before_c)
            before_c -= 1
        elif array[current] == order[1]:
            current += 1
        else:
            raise Exception("Number not appearing in order array")


def swap(array, index_a, index_b):
    array[index_b], array[index_a] = array[index_a], array[index_b]


def main():
    array = [2, 2, 1, 0, 1, 2, 0, 0, 0, 0, 1]
    order = [0, 1, 2]
    three_number_sort(array, order)
    print(array)


if __name__ == "__main__":
    main()
