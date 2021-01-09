def smallest_difference(array_1, array_2):
    local_array_1 = sorted(array_1)
    local_array_2 = sorted(array_2)

    index_1 = 0
    index_2 = 0
    solution = [local_array_1[index_1], local_array_2[index_2]]
    dif = abs(solution[0] - solution[1])
    while index_1 < len(local_array_1) and index_2 < len(local_array_2):
        if dif > abs(local_array_1[index_1] - local_array_2[index_2]):
            solution = [local_array_1[index_1], local_array_2[index_2]]
            dif = abs(solution[0] - solution[1])

        if local_array_1[index_1] < local_array_2[index_2]:
            index_1 += 1
        else:
            index_2 += 1

    return solution



def main():
    array1 = [-5, -1, -4, 2, -3, -2, 3]
    array2 = [12, 4, 78, -9, 1, 3, -6]
    print(smallest_difference(array1, array2))



if __name__ == "__main__":
    main()
