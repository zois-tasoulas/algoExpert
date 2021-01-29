def number_of_ways_to_make_change(n, denominations):
    ways_per_number = dict()
    ways_per_number[0] = 1
    for ii in range(1, n + 1):
        ways_per_number[ii] = 0

    for element in denominations:
        for ii in range(element, n + 1):
            ways_per_number[ii] += ways_per_number[ii - element]

    return ways_per_number[n]


def main():
    n = 11
    denominations = [1, 25, 5, 10]
    print(number_of_ways_to_make_change(n, denominations))


if __name__ == "__main__":
    main()
