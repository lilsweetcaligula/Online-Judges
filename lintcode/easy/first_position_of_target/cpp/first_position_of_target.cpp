/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/first-position-of-target
@Language: C++
@Datetime: 17-02-16 08:40
*/

class Solution {
public:
    /**
     * @param nums: The integer array.
     * @param target: Target number to find.
     * @return: The first position of target. Position starts from 0. 
     */
    int binarySearch(vector<int> &array, int target) 
    {
        decltype(array.size()) lo{ 0 };
        decltype(array.size()) hi{ array.size() };
        
        while (lo < hi)
        {
            const auto mid = lo + (hi - lo) / 2;
            
            if (target <= array[mid]) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        
        if (lo < array.size() && array[lo] == target) {
            return lo;
        }
        
        return -1;
    }
};