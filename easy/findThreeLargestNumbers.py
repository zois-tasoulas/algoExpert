def find_three_largest_numbers(array):
    amount_of_numbers = 3

    if len(array) < amount_of_numbers:
        raise Exception("Input array contains less than three elements")

    result = []
    for index in range(amount_of_numbers):
        result.append(None)
    for number in array:
        for index in range(amount_of_numbers - 1, -1, -1):
            if  result[index] is None or number > result[index]:
                for index_2 in range(0, index):
                    result[index_2] = result[index_2 + 1]
                result[index] = number
                break

    return result



def main():
    input_list = [1, 5, 2, 26, -4, 8, 0, 365, 79, -98]
    output_list = find_three_largest_numbers(input_list)
    print(output_list)



if __name__ == "__main__":
    main()
