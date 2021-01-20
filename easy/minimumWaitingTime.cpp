#include <algorithm>
#include <iostream>
#include <vector>

int minimumWaitingTime(std::vector<int> waitingTimes);

int main() {
    std::vector<int> waitingTimes{4, 3, 6, 1};
    int minimumTime{minimumWaitingTime(waitingTimes)};

    std::cout << minimumTime << std::endl;

    return 0;
}

int minimumWaitingTime(std::vector<int> waitingTimes) {
    sort(waitingTimes.begin(), waitingTimes.end());

    int accumulate{0};
    int totalWaitingTime{0};
    for (int index{1}; index < static_cast<int>(waitingTimes.size()); ++index) {
        accumulate += waitingTimes[index - 1];
        totalWaitingTime += accumulate;
    }

    return totalWaitingTime;
}
