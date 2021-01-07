def ceasar_cipher_encryptor(string, key):
    if string is None:
        raise Exception("Empty string passed to ceasar_cipher_encryptor")

    # The alphabet has 26 letters, keys will be kept between 0 and 24
    key = key % 26

    encrypted_string = ""
    for letter in string:
        if ord(letter) < ord('a') or ord(letter) > ord('z'):
            raise Exception("Non lower case letter found")

        encrypted_number = ord(letter) + key
        # Wrapping around the alphabet
        if encrypted_number > ord('z'):
            encrypted_number -= ord('z') - ord('a') + 1
        encrypted_string += chr(encrypted_number)

    return encrypted_string



def main():
    string = "helloz"
    key = 5
    encrypted_string = ceasar_cipher_encryptor(string, key)
    print(encrypted_string)



if __name__ == "__main__":
    main()
