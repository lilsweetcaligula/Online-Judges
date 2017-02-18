/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/reverse-words-in-a-string
@Language: C++
@Datetime: 17-02-15 19:12
*/

#include <sstream>
#include <vector>

class Solution {
public:
    /**
     * @param s : A string
     * @return : A string
     */
    std::string reverseWords(std::string s) 
    {
        std::vector<std::string> words;
        std::istringstream iss{ s };
        std::string result;
        
        for (std::string word; iss >> word; ) {
            words.push_back(word);
        }
        
        while (words.size() > 0) {
            result += words.back() + (words.size() > 1 ? " " : "");
            words.pop_back();
        }
        
        return result;
    }
};