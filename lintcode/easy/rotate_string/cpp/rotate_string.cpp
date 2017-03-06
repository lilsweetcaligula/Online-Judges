/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/rotate-string
@Language: C++
@Datetime: 17-02-15 19:16
*/

#include <algorithm>

class Solution {
public:
    /**
     * @param str: a string
     * @param offset: an integer
     * @return: nothing
     */
    void rotateString(std::string &str,int offset) 
    {
        if (str.size() == 0) {
            return;
        }
        
        const auto k = offset % str.size();
        std::reverse(str.begin(), str.end());
        std::reverse(str.begin(), str.begin() + k);
        std::reverse(str.begin() + k, str.end());
    }
};
