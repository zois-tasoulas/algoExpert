def is_palindrome(string):
    if string is None:
        raise Exception("Empty string passed to function is_palindrome")

    end_index = len(string) - 1

    # For odd length strings, the middle letter will not be checked
    for index in range(0, len(string) // 2):
        if string[index] != string[end_index - index]:
            return False

    return True



def main():
    strings = ["abba", "banana", "d", "asdfdsa", "zxcvbxz"]
    for word in strings:
        if is_palindrome(word):
            print(word, "is a palindrome")
        else:
            print(word, "is not a palindrome")



if __name__ == "__main__":
    main()
