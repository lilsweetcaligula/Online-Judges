/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/strstr
@Language: C++
@Datetime: 17-02-15 19:19
*/

class Solution {
public:
    /**
     * Returns a index to the first occurrence of target in source,
     * or -1  if target is not part of source.
     * @param source string to be scanned.
     * @param target string containing the sequence of characters to match.
     */
    int strStr(const char *source, const char *target) 
    {
        if (source == nullptr || target == nullptr) {
            return -1;
        }
        
        return std::string{ source }.find(target);
    }
};
