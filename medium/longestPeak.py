def longest_peak(array):
    if array is None or len(array) < 3:
        return 0

    lngst_peak = 0
    current_peak = 0

    prev = array[0]
    ascending = False
    descending = False
    for index in range(1, len(array)):
        if not ascending and not descending and array[index] > prev:
            current_peak += 2
            ascending = True
        elif ascending and array[index] == prev:
            current_peak = 0
            ascending = False
            descending = False
        elif ascending and array[index] > prev:
            current_peak += 1
        elif ascending and array[index] < prev:
            current_peak += 1
            lngst_peak = max(lngst_peak, current_peak)
            ascending = False
            descending = True
        elif descending and array[index] == prev:
            current_peak = 0
            descending = False
        elif descending and array[index] < prev:
            current_peak += 1
            lngst_peak = max(lngst_peak, current_peak)
        elif descending and array[index] > prev:
            current_peak = 2
            ascending = True
            descending = False

        prev = array[index]

    return lngst_peak


def main():
    array = [1, 0, -5, 4, 7, 9, -4, -7, -17, -17, -18, 12]
    print(longest_peak(array))


if __name__ == "__main__":
    main()
