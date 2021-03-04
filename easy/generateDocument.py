from collections import defaultdict


def generate_document(string, document):
    d = defaultdict(lambda: 0)

    for letter in string:
        d[letter] += 1

    for letter in document:
        if d[letter] < 1:
            return False

        d[letter] -= 1

    return True


def main():
    string = "lloorldWHe! "
    document = "Hello World!"

    print(generate_document(string, document))


if __name__ == "__main__":
    main()
