/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/longest-words
@Language: C++
@Datetime: 17-02-15 15:52
*/

#include <algorithm>

class Solution {
public:
    /**
     * @param dict: a vector of strings
     * @return: a vector of strings
     */
    std::vector<std::string> longestWords(std::vector<std::string> &dict)
    {
        std::vector<std::string> result;
        
        const auto maxLength = max_element(dict.cbegin(), dict.cend(),
            [] (decltype(*dict.cbegin()) left, decltype(*dict.cbegin()) right) {
                return left.size() < right.size();
            })->size();
            
        for (const auto &str : dict) {
            if (str.size() == maxLength) {
                result.push_back(str);
            }
        }
        
        
        return result;
    }
};