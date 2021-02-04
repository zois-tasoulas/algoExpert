#include <iostream>
#include <vector>

bool singleCycleCheck(std::vector<int> array) {
    long unsigned int visitedElements{0};
    int index{0};

    while (visitedElements < array.size()) {
        visitedElements += 1;
        if ((index == 0) && (visitedElements > 1)) {
            return false;
        }

        index = (index + array[index]) % static_cast<int>(array.size());
        if (index < 0) {
            index = array.size() + index;
        }
    }

    return index == 0 ? true : false;
}

int main() {
    std::vector<int> array{1, 2, 3, 1, -2};

    std::cout << std::boolalpha;
    std::cout << singleCycleCheck(array) << std::endl;

    return 0;
}
