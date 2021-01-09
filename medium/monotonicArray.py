def monotonic_array(array):
    increasing = False
    decreasing = False

    if array is not None:
        for index in range(1, len(array)):
            if array[index - 1] > array[index]:
                increasing = True
            elif array[index - 1] < array[index]:
                decreasing = True

            if increasing and decreasing:
                break

    return not (increasing and decreasing)



def main():
    array = [1, 2, 2, 3, 3, 3, 4, 7, 19, 25, 25, 678]
    print("Is", array, "monotonic?:", monotonic_array(array))
    array_2 = [1, 2, 2, 3, 19, 25, 25, -1, 678]
    print("Is", array_2, "monotonic?:", monotonic_array(array_2))



if __name__ == "__main__":
    main()
