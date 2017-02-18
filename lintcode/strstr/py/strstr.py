# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/strstr
@Language: Python
@Datetime: 17-02-15 15:05
'''

class Solution:
    def strStr(self, source, target):
        return source.find(target) if None not in (source, target) else -1