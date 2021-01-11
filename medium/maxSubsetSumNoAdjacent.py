def max_subset_sum_no_adjacent(array):
    if not array:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        max_sums = [array[0], max(array[0], array[1])]
        for index in range(2, len(array)):
            temp = max_sums[1]
            max_sums[1] = max(max_sums[0] + array[index], max_sums[1])
            max_sums[0] = temp
        return max(max_sums)



def main():
    array = [1, 2, 3, 4, 5, 6, 7, 8]
    print(max_subset_sum_no_adjacent(array))



if __name__ == "__main__":
    main()
