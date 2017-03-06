# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/longest-increasing-continuous-subsequence
@Language: Python
@Datetime: 17-02-16 10:17
'''

class Solution:
    def longestSubsequence(self, A, cmp):
        maxcount = 0
        count    = 0
        
        i = 0
        
        while i < len(A):
            j = i
            count = 1
            
            while j + 1 < len(A) and cmp(A[j], A[j + 1]):
                count += 1
                j += 1
                
            maxcount = max(maxcount, count)
            i = j + 1
        
        return maxcount
        
        
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        return max( self.longestSubsequence(A, lambda x, y: x <= y),
                    self.longestSubsequence(A, lambda x, y: x >= y))