/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/count-and-say
@Language: C++
@Datetime: 17-02-15 16:52
*/

#include <utility>
#include <sstream>
#include <algorithm>

class Solution {
public:
    /**
     * @param n the nth
     * @return the nth sequence
     */
    std::string countAndSay(int n) 
    {
        std::string s{ "1" };
            
        while (n-- > 1) 
        {        
            std::string t;
            
            for (decltype(s.size()) i{ 1 }, count{ 1 }; i <= s.size(); ++i, ++count) 
            {
                if (i == s.size() || (s[i] != s[i - 1])) 
                {
                    std::ostringstream oss;
                    oss << count;
                    t += oss.str() + s[i - 1];
                    count = 0;
                }
            }
    
            s = std::move(t);
        }
            
        return s;
    }
};