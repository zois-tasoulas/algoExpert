def swap(index_a, index_b, array):
    array[index_b], array[index_a] = array[index_a], array[index_b]



def insertion_sort(input_array):
    array = input_array[:]

    for ii in range(len(array)):
        for jj in range(ii, 0, -1):
            if array[jj] < array[jj - 1]:
                swap(jj - 1, jj, array)

    return array



def main():
    input_array = [5, 6, 3, 8, 7, 1, 4, 9, 2, 0]
    sorted_array = insertion_sort(input_array)
    print(sorted_array)



if __name__ == "__main__":
    main()
