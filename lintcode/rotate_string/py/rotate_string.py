# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/rotate-string
@Language: Python
@Datetime: 17-02-15 15:07
'''

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        if len(s) == 0:
            return
        
        k     = offset % len(s)
        s[:]  = s[::-1]
        s[:k] = reversed(s[:k])
        s[k:] = reversed(s[k:])