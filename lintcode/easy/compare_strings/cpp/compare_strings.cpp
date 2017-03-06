/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/compare-strings
@Language: C++
@Datetime: 17-02-15 18:32
*/

#include <map>

class Solution {
public:
    /**
     * @param A: A string includes Upper Case letters
     * @param B: A string includes Upper Case letter
     * @return:  if string A contains all of the characters in B return true 
     *           else return false
     */
    bool compareStrings(string A, string B) 
    {
        std::map<char, int> freqs;
        
        for (const auto c : A) {
            ++freqs[c];
        }
        
        for (const auto c : B) {
            if (freqs[c] == 0) {
                return false;
            } else {
                --freqs[c];
            }
        }
        
        return true;
    }
};
