class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Without this check, the function
        # will return slow + 1 when called
        # with an empty array. This would
        # be an error.        
        if len(nums) == 0:
            return 0
        
        slow = 0
        
        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow      += 1
                nums[slow] = nums[fast]
                
        return slow + 1
