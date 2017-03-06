# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/longest-words
@Language: Python
@Datetime: 17-02-15 13:55
'''

class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        ordered = sorted(dictionary, key=len, reverse=True)
        words   = []
        
        for i in range(len(ordered)):
            words.append(ordered[i])
            
            if i + 1 < len(ordered) and len(ordered[i]) != len(ordered[i + 1]):
                break
                
        return words