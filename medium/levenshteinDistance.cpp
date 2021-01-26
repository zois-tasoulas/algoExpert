#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int levenshteinDistance(const std::string &string1, const std::string &string2);

int main() {
    std::string string1{"asdfg"};
    std::string string2{"asrthg"};

    std::cout << levenshteinDistance(string1, string2) << std::endl;

    return 0;
}

int levenshteinDistance(const std::string &string1,
                        const std::string &string2) {
    std::vector<std::vector<int>> solution(
        string1.length() + 1, std::vector<int>(string2.length() + 1, 0));

    // Initialize first row
    for (int ii{0}; static_cast<long unsigned int>(ii) < (string2.length() + 1);
         ++ii) {
        solution[0][ii] = ii;
    }

    // Initialize first column
    for (int ii{0}; static_cast<long unsigned int>(ii) < (string1.length() + 1);
         ++ii) {
        solution[ii][0] = ii;
    }

    for (int ii{1}; static_cast<long unsigned int>(ii) < (string1.length() + 1);
         ++ii) {
        for (int jj{1};
             static_cast<long unsigned int>(jj) < (string2.length() + 1);
             ++jj) {
            if (string1[ii - 1] == string2[jj - 1]) {
                solution[ii][jj] = solution[ii - 1][jj - 1];
            } else {
                solution[ii][jj] =
                    std::min({solution[ii - 1][jj - 1], solution[ii][jj - 1],
                              solution[ii - 1][jj]}) +
                    1;
            }
        }
    }

    return solution[string1.length()][string2.length()];
}
