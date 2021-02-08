def reverse_words_in_string(string):
    whitespaces = " \n\t\r"

    words = []
    word = ""
    for char in string:
        if char in whitespaces:
            words = [word] + words
            word = ""
            words = [char] + words
        else:
            word = word + char

    # In case last character of the input string is not a whitespace
    words = [word] + words
    return "".join(words)


def main():
    string = "Git is a great\nversion\t  control tool!"
    print(reverse_words_in_string(string))


if __name__ == "__main__":
    main()
