def non_constructible_change(coins):
    if coins is None:
        return 1

    coins.sort()
    min_value = 0
    for coin in coins:
        if coin > min_value + 1:
            break
        else:
            min_value += coin

    return min_value + 1


def main():
    coins = [5, 2, 1, 20, 10]
    print(non_constructible_change(coins))


if __name__ == "__main__":
    main()
