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
        // Selection sort.
        
        for (decltype(A.size()) i{ 0 }; i < A.size(); ++i) 
        {
            auto min = i;
            
            for (auto j = i; j < A.size(); ++j) {
                min = std::min(j, min, 
                    [&A] (decltype(j) left, decltype(j) right) {
                        return A[left] < A[right];
                    });
            }
            
            std::swap(A[i], A[min]);
        }
    }
};
