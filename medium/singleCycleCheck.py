def single_cycle_check(array):
    counter = [0 for x in range(len(array))]

    # Setting counter of index 0 as -1 as this will be our starting point
    # If element at index 0 becomes 1, we should check for the cycle property
    counter[0] = -1
    index = 0
    while True:
        counter[index] += 1
        if counter[index] == 2:
            return False
        elif index == 0 and counter[index] == 1:
            return counter.count(1) == len(counter)

        index = (index + array[index]) % len(array)
        if index < 0:
            index = len(array) + index


def main():
    array = [1, 2, 3, 1, -2]
    print(single_cycle_check(array))


if __name__ == "__main__":
    main()
