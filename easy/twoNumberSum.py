def two_number_sum(array, target_sum):
    numbers_dictionary = {}
    solution_array = []
    for number in array:
        if target_sum - number in numbers_dictionary:
            solution_array = [number, target_sum - number]
            break
        else:
            numbers_dictionary[number] = True

    return solution_array

def main():
    input_array = [4, 3, 5, 8, 9, -1, 13]
    target_sum = 14
    solution_array = two_number_sum(input_array, target_sum)
    print(solution_array)

if __name__ == '__main__':
    main()
