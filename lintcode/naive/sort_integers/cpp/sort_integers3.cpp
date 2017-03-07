#include <algorithm>
#include <vector>

class Solution {
public:
    /**
     * @param A an integer array
     * @return void
     */
    void sortIntegers(std::vector<int>& A) 
    {
        // Insertion sort.

        for (decltype(A.size()) i{ 1 }; i < A.size(); ++i) 
        {
            for (auto j = i; j > 0; --j) {
                if (A[j] < A[j - 1]) {
                    std::swap(A[j], A[j - 1]);
                } else {
                    break;
                }
            }
        }
        
    }
};
