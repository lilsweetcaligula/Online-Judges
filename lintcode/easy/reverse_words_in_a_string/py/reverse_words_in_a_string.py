# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/reverse-words-in-a-string
@Language: Python
@Datetime: 17-02-15 15:03
'''

class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))