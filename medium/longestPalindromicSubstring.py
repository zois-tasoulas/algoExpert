def longest_palindromic_substring_dp(string):
    dp_array = [[0 for _ in range(len(string))] for _ in range(len(string))]

    longest_palindrome = "" if not string else string[0]
    # Setting diagonal to 1
    for index in range(len(string)):
        dp_array[index][index] = 1
    # Finding palindroms of length 2
    for index in range(len(string) - 1):
        if string[index] == string[index + 1]:
            dp_array[index][index + 1] = 1
            longest_palindrome = string[index : index + 2]

    for ii in range(len(string) - 2, -1, -1):
        for jj in range(len(string) - 1, ii, -1):
            if string[ii] == string[jj] and dp_array[ii + 1][jj - 1]:
                dp_array[ii][jj] = 1
                substring = string[ii : jj + 1]
                if len(substring) > len(longest_palindrome):
                    longest_palindrome = substring

    return longest_palindrome


def longest_palindromic_substring(string):
    if string is None or len(string) < 1:
        return ""

    max_length = 0
    start = 0
    end = 0
    for index in range(len(string)):
        odd_length = check_substring(string, index, index)
        even_length = check_substring(string, index, index + 1)

        if odd_length[1] - odd_length[0] > even_length[1] - even_length[0]:
            max_substring = odd_length[1] - odd_length[0] + 1
            current_start = odd_length[0]
            current_end = odd_length[1]
        else:
            max_substring = even_length[1] - even_length[0] + 1
            current_start = even_length[0]
            current_end = even_length[1]

        if max_substring > max_length:
            max_length = max_substring
            start = current_start
            end = current_end

    return string[start : end + 1]


def check_substring(string, start, end):
    left = start
    right = end

    while left >= 0 and right <= len(string) - 1:
        if string[left] != string[right]:
            break
        left -= 1
        right += 1

    return (left + 1, right - 1)


def main():
    string = "banana"
    print(longest_palindromic_substring(string))


if __name__ == "__main__":
    main()
