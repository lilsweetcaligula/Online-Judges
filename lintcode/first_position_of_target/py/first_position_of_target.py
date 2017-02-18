# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/first-position-of-target
@Language: Python
@Datetime: 17-02-16 08:33
'''

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        lo = 0
        hi = len(nums)
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if target <= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
                
        if lo < len(nums) and nums[lo] == target:
            return lo
            
        return -1