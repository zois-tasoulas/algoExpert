def valid_ip_addresses(string):
    ip_addresses = create_ip_addresses(string, 0, 3)

    solution = []
    for address in ip_addresses:
        if is_valid(address):
            solution.append(address)

    return solution


def create_ip_addresses(string, start, dots):
    addresses = []

    if dots == 0:
        return [string[start:]]

    if start > len(string) - 1:
        return addresses

    for index in range(1, 4):
        current_addresses = create_ip_addresses(string, start + index, dots - 1)
        for a_index, address in enumerate(current_addresses):
            current_addresses[a_index] = string[start : start + index] + "." + address
            addresses.append(current_addresses[a_index])

    return addresses


def is_valid(address):
    parts = address.split(".")
    for part in parts:
        if len(part) > 4 or len(part) < 1:
            return False
        if len(part) > 1 and part[0] == "0":
            return False
        if int(part) > 255:
            return False

    return True


def main():
    string = "1234512253"
    print(valid_ip_addresses(string))


if __name__ == "__main__":
    main()
