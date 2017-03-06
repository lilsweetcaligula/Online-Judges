/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/length-of-last-word
@Language: C++
@Datetime: 17-02-15 16:14
*/

#include <vector>
#include <sstream>

class Solution {
public:
    /**
     * @param s A string
     * @return the length of last word
     */
    int lengthOfLastWord(std::string& s) 
    {
        std::vector<std::string> words;
        std::istringstream iss { s };
        std::string word;
    
        while (iss >> word) {
            words.push_back(word);
        }
            
        if (words.size() == 0) {
            return 0;
        }
            
        return words.back().size();
    }
};