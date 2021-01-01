def binary_search(array, target):
    index = -1
    left_boundary = 0
    right_boundary = len(array) - 1
    while left_boundary <= right_boundary:
        median = (right_boundary + left_boundary) // 2
        if target == array[median]:
            index = median
            break
        elif target < array[median]:
            right_boundary = median - 1
        else:
            left_boundary = median + 1


    return index



def main():
    print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 12))
    print(binary_search([1, 12, 23, 34, 45, 56, 67, 68], 12))



if __name__ == "__main__":
    main()
