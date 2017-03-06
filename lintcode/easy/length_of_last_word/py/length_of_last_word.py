# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/length-of-last-word
@Language: Python
@Datetime: 17-02-15 13:57
'''

class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        words = s.split()
        
        if len(words) == 0:
            return 0
        
        return len(words[-1])