#include <algorithm>
#include <iostream>
#include <vector>

int kadanesAlgorithm(const std::vector<int> &array);

int main() {
    std::vector<int> array{1, -6, 4, 3, -3, 8};

    std::cout << kadanesAlgorithm(array) << std::endl;
}

int kadanesAlgorithm(const std::vector<int> &array) {
    int accumulate{array[0]};
    int maxSum{accumulate};

    for (int i{1}; i < static_cast<int>(array.size()); ++i) {
        accumulate = std::max(accumulate + array[i], array[i]);
        maxSum = std::max(maxSum, accumulate);
    }

    return maxSum;
}
