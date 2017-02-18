# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/count-and-say
@Language: Python
@Datetime: 17-02-15 14:07
'''

class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        def helper(n, s='1'):
            import itertools
                
            if n <= 1:
                return s
                
            t = ''
            
            for c, g in itertools.groupby(s):
                t += str(len(tuple(g))) + c
                
            return helper(n - 1, t)
        
        if n == 0:
            return ''
            
        return helper(n)