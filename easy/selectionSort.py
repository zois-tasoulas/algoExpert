def swap(index_a, index_b, array):
    array[index_b], array[index_a] = array[index_a], array[index_b]



def find_min(start_index, array):
    index = start_index
    for ii in range(start_index + 1, len(array)):
        if array[index] > array[ii]:
            index = ii

    return index



def selection_sort(input_array):
    array = input_array[:]

    for ii, _ in enumerate(array):
        min_index = find_min(ii, array)
        if array[ii] > array[min_index]:
            swap(ii, min_index, array)

    return array



def main():
    input_array = [5, 6, 3, 8, 7, 1, 4, 9, 2, 0]
    sorted_array = selection_sort(input_array)
    print(sorted_array)



if __name__ == "__main__":
    main()
