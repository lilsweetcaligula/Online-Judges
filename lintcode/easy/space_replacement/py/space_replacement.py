# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/space-replacement
@Language: Python
@Datetime: 17-02-15 13:39
'''

class Solution:
    # @param {char[]} chars: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, chars, length):
        if chars == None:
            return None
        
        buff = chars[:length]
        j    = 0
        
        for i in range(len(buff)):
            if buff[i] == ' ':
                for c in '%20':
                    chars[j] = c
                    j += 1
            else:
                chars[j] = buff[i]
                j += 1
                
        return j