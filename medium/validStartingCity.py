def validate_city(city, distances, fuel, mpg):
    number_of_cities = len(distances)
    remaining_miles = 0

    for index in range(number_of_cities):
        current_city = (
            (index + city)
            if index + city < number_of_cities
            else (index + city) % number_of_cities
        )
        remaining_miles = (
            remaining_miles + fuel[current_city] * mpg - distances[current_city]
        )
        if remaining_miles < 0:
            return False

    return True


def valid_starting_city(distances, fuel, mpg):
    for city in range(len(distances)):
        if validate_city(city, distances, fuel, mpg):
            return city

    raise Exception("No valid startin city exists")


def main():
    mpg = 27
    distances = [27, 135, 54, 81]
    fuel = [2, 3, 1, 5]

    print(valid_starting_city(distances, fuel, mpg))


if __name__ == "__main__":
    main()
