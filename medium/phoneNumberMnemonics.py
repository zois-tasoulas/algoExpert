def phone_number_mnemonics(number):
    mnemonics = [""]

    for digit in number:
        mappings = map_digit_to_char(digit)
        new_mnemonics = []
        for mnemonic in mnemonics:
            for char in mappings:
                new_mnemonics.append(mnemonic + char)

        mnemonics = new_mnemonics[:]

    return mnemonics


def map_digit_to_char(digit):
    if digit == "0":
        chars = ["0"]
    elif digit == "1":
        chars = ["1"]
    elif digit == "2":
        chars = ["a", "b", "c"]
    elif digit == "3":
        chars = ["d", "e", "f"]
    elif digit == "4":
        chars = ["g", "h", "i"]
    elif digit == "5":
        chars = ["j", "k", "l"]
    elif digit == "6":
        chars = ["m", "n", "o"]
    elif digit == "7":
        chars = ["p", "q", "r", "s"]
    elif digit == "8":
        chars = ["t", "u", "v"]
    elif digit == "9":
        chars = ["w", "x", "y", "z"]
    else:
        raise Exception("Unexpected character received")

    return chars


def main():
    phone_number = "618"
    mnemonics = phone_number_mnemonics(phone_number)
    for string in mnemonics:
        print(string)


if __name__ == "__main__":
    main()
