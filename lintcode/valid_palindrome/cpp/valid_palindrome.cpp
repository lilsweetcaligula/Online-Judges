/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/valid-palindrome
@Language: C++
@Datetime: 17-02-15 17:17
*/

#include <locale>

class Solution {
public:
    /**
     * @param s A string
     * @return Whether the string is a valid palindrome
     */
    bool isPalindrome(std::string& s) 
    {
        if (s.size() == 0) {
            return true;    
        }
        
        const std::locale loc;
        
        decltype(s.size()) i { 0 };
        decltype(s.size()) j { s.size() - 1 };
        
        while (i < j) 
        {
            if (std::isalnum(s[i], loc) && std::isalnum(s[j], loc)) {
                if (std::tolower(s[i], loc) != std::tolower(s[j], loc)) {
                    return false;
                }
                ++i; --j;
            } else if (std::isalnum(s[i], loc)) {
                --j;
            } else if (std::isalnum(s[j], loc)) {
                ++i;   
            } else {
                ++i; --j;
            }
        }
        
        return true;
    }
};