def balanced_brackets(string):
    bracket_match = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in string:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack:
                return False

            if stack.pop(-1) != bracket_match[char]:
                return False
        else:
            # For all other character do nothing
            continue

    return not stack


def main():
    string = "({[()()([[[]]{()}])]})"
    print(balanced_brackets(string))
    string = "{{{[()]([()])}}(})"
    print(balanced_brackets(string))


if __name__ == "__main__":
    main()
