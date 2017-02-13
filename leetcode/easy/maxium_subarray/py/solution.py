class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
                
        maxSub   = nums[0]
        maxSoFar = nums[0]
            
        for index in range(1, len(nums)):
                
            maxSoFar = max(nums[index], maxSoFar + nums[index])
            maxSub   = max(maxSub,      maxSoFar)
                
        return maxSub
