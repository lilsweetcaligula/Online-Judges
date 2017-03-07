#include <algorithm>
#include <vector>

class Solution {
public:
    /**
     * @param A an integer array sorted in ascending order
     * @param target an integer
     * @return an integer
     */
    int findPosition(std::vector<int>& A, int target) 
    {
        decltype(A.size()) lo{ 0 };
        decltype(A.size()) hi{ A.size() };
        
        while (lo < hi) 
        {
            const auto mid = lo + (hi - lo) / 2;
            
            if (A[mid] > target) {
                hi = mid;
            } else if (A[mid] < target) {
                lo = mid + 1;
            } else {
                return mid;   
            }
        }
        
        return -1;
    }
};
