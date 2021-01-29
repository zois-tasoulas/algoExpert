def product_sum(array, level=1):
    array_sum = 0
    for element in array:
        if isinstance(element, int):
            array_sum += element
        elif isinstance(element, list):
            array_sum += product_sum(element, level + 1)
        else:
            raise Exception("Wrong type for array element")

    return level * array_sum


def main():
    # Expected result 146
    print(product_sum([1, 2, 3, [4, 5], 6, [7, [8, 9]]]))


if __name__ == "__main__":
    main()
