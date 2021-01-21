#include <iostream>
#include <vector>

int minNumberOfCoinsForChange(std::vector<int> denominations, int n);

int main() {
    int n{78};
    std::vector<int> denominations{5, 1, 10, 50, 25};

    std::cout << minNumberOfCoinsForChange(denominations, n) << std::endl;

    return 0;
}

int minNumberOfCoinsForChange(std::vector<int> denominations, int n) {
    std::vector<int> amounts(n + 1, -1);

    amounts[0] = 0;
    for (int coin : denominations) {
        for (int amount{1}; amount < static_cast<int>(amounts.size());
             ++amount) {
            if (amount < coin) {
                continue;
            }
            if (amounts[amount - coin] != -1 &&
                (amounts[amount] == -1 ||
                 (amounts[amount] > amounts[amount - coin] + 1))) {
                amounts[amount] = amounts[amount - coin] + 1;
            }
        }
    }

    return amounts[n];
}
