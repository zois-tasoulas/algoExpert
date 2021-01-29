def is_valid_subsequence(array, subarray):
    if len(subarray) > len(array):
        return False

    index = 0
    for number in subarray:
        while (index < len(array)) and (array[index] != number):
            index += 1
        # Incrementing index once outside of the while loop so next iteration
        # checks the next element
        if index >= len(array):
            return False
        index += 1

    return True


def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    subarray = [2, 6, 8]
    if is_valid_subsequence(array, subarray):
        print("The subarray is a valid subsequence")
    else:
        print("The subarray is not a valid subsequence")
    subarray = [12, -6, 8, 15, 56]
    if is_valid_subsequence(array, subarray):
        print("The subarray is a valid subsequence")
    else:
        print("The subarray is not a valid subsequence")


if __name__ == "__main__":
    main()
