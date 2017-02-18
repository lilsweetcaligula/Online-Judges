/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/add-binary
@Language: C++
@Datetime: 17-02-15 18:17
*/

#include <iterator>

class Solution {
public:
    /**
     * @param a a number
     * @param b a number
     * @return the result
     */
    std::string addBinary(std::string& left, std::string& right)
    {
        static const int BASE{ 2 };
        
        std::string result;
        
        auto i = left.size();
        auto j = right.size();
        int carry{ 0 };
        
        while (i > 0 || j > 0)
        {
            const auto leftVal  = i > 0 ? left[i-- - 1] - '0' : 0;
            const auto rightVal = j > 0 ? right[j-- - 1] - '0' : 0;
            const auto sum      = leftVal + rightVal + carry;
            
            result += sum % BASE + '0';
            carry   = sum / BASE;
        }
        
        if (carry) {
            result += carry % BASE + '0';
        }
        
        return {
            std::reverse_iterator<std::string::const_iterator>{ result.cend() },
            std::reverse_iterator<std::string::const_iterator>{ result.cbegin() }
        };
    }
};