# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/two-strings-are-anagrams
@Language: Python
@Datetime: 17-02-15 14:51
'''

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        import collections
        return len(collections.Counter(s) - collections.Counter(t)) == 0
        