# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/valid-palindrome
@Language: Python
@Datetime: 17-02-15 14:09
'''

class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        t = tuple(c.lower() for c in s if c.isalnum())
        return t == t[::-1]