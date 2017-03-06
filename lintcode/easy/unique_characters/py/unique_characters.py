# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/unique-characters
@Language: Python
@Datetime: 17-02-15 14:58
'''

class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, s):
        ordered = sorted(s)
        
        for i in range(1, len(ordered)):
            if ordered[i] == ordered[i - 1]:
                return False
                
        return True
    