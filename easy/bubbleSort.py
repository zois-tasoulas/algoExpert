def swap(index_a, index_b, array):
    array[index_b], array[index_a] = array[index_a], array[index_b]



def bubble_sort(input_array):
    array = input_array[:]
    for ii in range(len(array)):
        one_swap = False
        for jj in range(1, len(array) - ii):
            if array[jj - 1] > array[jj]:
                swap(jj - 1, jj, array)
                one_swap = True
        if not one_swap:
            break
    return array



def main():
    input_list = [5, 6, 3, 8, 7, 1, 4, 9, 2, 0]
    sorted_list = bubble_sort(input_list)
    print(sorted_list)



if __name__ == "__main__":
    main()
