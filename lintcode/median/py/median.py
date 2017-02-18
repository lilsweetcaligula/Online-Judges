# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/median
@Language: Python
@Datetime: 17-02-16 11:26
'''

class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        if len(nums) == 0:
            return 0
        
        ordered = sorted(nums)
        
        if len(nums) % 2:
            return ordered[len(ordered) // 2]
            
        return ordered[len(ordered) // 2 - 1]