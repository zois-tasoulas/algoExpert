def min_number_of_coins_for_change(denominations, n):
    amounts = [-1 for _ in range(n + 1)]
    amounts[0] = 0
    for coin in denominations:
        for amount in range(1, len(amounts)):
            if amount < coin:
                continue
            if  amounts[amount - coin] != -1 and \
                (amounts[amount] == -1 or
                 amounts[amount] > amounts[amount - coin] + 1):

                amounts[amount] = amounts[amount - coin] + 1

    return amounts[n]



def main():
    amount = 78
    denominations = [5, 10, 1, 25, 50]
    print(min_number_of_coins_for_change(denominations, amount))



if __name__ == "__main__":
    main()
