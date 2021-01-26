def levenshtein_distance(string1, string2):
    solution = [[0 for index_2 in range(len(string2) + 1)] for index_1 in range(len(string1) + 1)]

    # Initialize first row
    for index in range(len(string2) + 1):
        solution[0][index] = index

    # Initialize first column
    for index in range(len(string1) + 1):
        solution[index][0] = index

    for row in range(1, len(string1) + 1):
        for column in range(1, len(string2) + 1):
            if string1[row - 1] == string2[column - 1]:
                solution[row][column] = solution[row - 1][column - 1]
            else:
                solution[row][column] = min(solution[row - 1][column - 1],
                                            solution[row - 1][column],
                                            solution[row][column - 1]) + 1

    return solution[-1][-1]



def main():
    string1 = "asdfg"
    string2 = "asrthg"

    print(levenshtein_distance(string1, string2))



if __name__ == "__main__":
    main()
