def kadanes_algorithm(array):
    accumulate = array[0]
    max_sum = accumulate

    for index in range(1, len(array)):
        accumulate = max(accumulate + array[index], array[index])
        max_sum = max(max_sum, accumulate)

    return max_sum


def main():
    array = [1, -6, 4, 3, -3, 8]
    print(kadanes_algorithm(array))


if __name__ == "__main__":
    main()
