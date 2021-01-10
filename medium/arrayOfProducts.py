def array_of_products(array):
    '''
    The first sublist element denotes the product on the left of the number
    The second sublist element denotes the product on the right of the number
    '''
    accumulated_products = [[1, 1]]
    # Setting the product on the left of each number
    for index in range(1, len(array)):
        accumulated_products.append([accumulated_products[index - 1][0] * array[index - 1], 1])

    # Setting the product on the right of each number
    for index in range(len(array) - 2, -1, -1):
        accumulated_products[index][1] = accumulated_products[index + 1][1] * array[index + 1]

    solution = []
    for element in accumulated_products:
        solution.append(element[0] * element[1])

    return solution



def main():
    array = [1, 2, 3, 4, 5, 6]
    print(array_of_products(array))



if __name__ == "__main__":
    main()
