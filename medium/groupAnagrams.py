def group_anagrams(array):
    anagrams = dict()

    for string in array:
        sorted_string = "".join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]

    return list(anagrams.values())


def main():
    array = ["oof", "orwd", "bar", "ofo", "arb", "hello", "word", "helo"]
    print(group_anagrams(array))


if __name__ == "__main__":
    main()
