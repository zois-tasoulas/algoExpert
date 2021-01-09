def three_number_sum(array, number):
    local = sorted(array)

    # We can exlude the two last elements since we are looking for triplets
    solution = []
    for index in range(len(local) - 2):
        left_limit = index + 1
        right_limit = len(local) - 1
        while left_limit < right_limit:
            current_sum = local[index] + local[left_limit] + local[right_limit]
            if current_sum == number:
                solution.append([local[index], local[left_limit], local[right_limit]])
                left_limit += 1
                right_limit -= 1
            elif current_sum > number:
                right_limit -= 1
            else:
                # current_sum < num
                left_limit += 1

    return solution



def main():
    number = 8
    array = [1, 0, 6, 2, 5, 3, 4]
    solutions = three_number_sum(array, number)
    print(solutions)
    array = [1, 0, 2, 3]
    solutions = three_number_sum(array, number)
    print(solutions)



if __name__ == "__main__":
    main()
