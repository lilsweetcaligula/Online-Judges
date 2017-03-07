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
        // Bubble sort.
        
        auto wasSwapped = false;
        
        for (decltype(A.size()) i{ 0 }; i < A.size(); ++i) 
        {
            for (auto j = i; j < A.size(); ++j) 
            {
                if (A[j] < A[i]) {
                    std::swap(A[i], A[j]);
                    wasSwapped = true;
                }
            }
            
            if (!wasSwapped) break;
        }
    }
};
