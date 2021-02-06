def permutations(array):
    if not array:
        return []

    perms = []
    create_permutations(array, 0, perms)
    return perms


def create_permutations(array, index_i, perms):
    if index_i == len(array) - 1:
        perms.append(array[:])
    else:
        for index_j in range(index_i, len(array)):
            swap(array, index_i, index_j)
            create_permutations(array, index_i + 1, perms)
            swap(array, index_i, index_j)


def swap(array, index_i, index_j):
    array[index_i], array[index_j] = array[index_j], array[index_i]


def main():
    array = [10, 11, 12]
    print(permutations(array))


if __name__ == "__main__":
    main()
