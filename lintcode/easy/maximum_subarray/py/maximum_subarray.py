# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/maximum-subarray
@Language: Python
@Datetime: 17-02-16 10:36
'''

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0
            
        maxHere  = nums[0]
        maxSoFar = maxHere
            
        for i in range(1, len(nums)):
            maxHere  = max(maxHere + nums[i], nums[i])
            maxSoFar = max(maxSoFar, maxHere)
                
        return maxSoFar