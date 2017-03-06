/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/unique-characters
@Language: C++
@Datetime: 17-02-15 18:27
*/

#include <algorithm>

class Solution {
public:
    /**
     * @param str: a string
     * @return: a boolean
     */
    bool isUnique(std::string str) 
    {
        std::sort(str.begin(), str.end());
        
        for (decltype(str.size()) i{ 1 }; i < str.size(); ++i) {
            if (str[i] == str[i - 1]) {
                return false;
            }
        }
        
        return true;
    }
};