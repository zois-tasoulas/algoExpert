def run_length_encoding(string):
    if string is None:
        raise Exception("Empty string passed to run_length_encoding function")

    encoded_string = ""
    counter = 0
    for index, letter in enumerate(string):
        if index == 0:
            counter = 1
        elif counter == 9 or letter != string[index - 1]:
            encoded_string += str(counter) + string[index - 1]
            counter = 1
        else:
            counter += 1

        if index == len(string) - 1:
            encoded_string += str(counter) + string[index]

    return encoded_string



def main():
    input_string = "aaasssssDfDDDDDDDDDD"
    encoded_string = run_length_encoding(input_string)
    print(encoded_string)



if __name__ == "__main__":
    main()
