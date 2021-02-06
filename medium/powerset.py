def powerset(array):
    sets = []
    create_powerset(array, 0, sets)
    return sets


def create_powerset(array, index, sets):
    if not array or index == len(array):
        sets.append([])
    else:
        create_powerset(array, index + 1, sets)
        new_sets = []
        for member in sets:
            new_sets.append(member + [array[index]])
        for member in new_sets:
            sets.append(member)


def main():
    array = [10, 11, 12, 13]
    print(powerset(array))


if __name__ == "__main__":
    main()
