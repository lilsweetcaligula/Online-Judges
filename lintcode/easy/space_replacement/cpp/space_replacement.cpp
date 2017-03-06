/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/space-replacement
@Language: C++
@Datetime: 17-02-15 15:49
*/

class Solution {
public:
    /**
     * @param string: An array of Char
     * @param length: The true length of the string
     * @return: The true length of new string
     */
    int replaceBlank(char string[], int length) 
    {
        static const std::string repl { "%20" };
        const std::vector<char> buffer { &string[0], &string[length] };
        int index { 0 };
        
        for (const auto ch : buffer) {
            if (ch == ' ') {
                for (const auto replCh : repl) {
                    string[index++] = replCh;
                }
            } else {
                string[index++] = ch;   
            }
        }
        
        return index;
    }
};