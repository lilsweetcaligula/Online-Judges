/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/two-strings-are-anagrams
@Language: C++
@Datetime: 17-02-15 18:24
*/

#include <algorithm>

class Solution {
public:
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    bool anagram(std::string s, std::string t) 
    {
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        
        return s == t;
    }
};