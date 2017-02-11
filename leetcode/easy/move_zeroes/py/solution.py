class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0

        while fast < len(nums):        
            # If nums[fast] is not 0, copy the value to nums[slow]
            # and move the fast index a step further.
            
            if nums[fast] != 0:
                nums[slow]  = nums[fast]
                slow       += 1
                
            fast += 1

      
        # All non-zero values have been placed to the left of the slow
        # index now at this point. Fill the remainder of the array with
        # zeros to overwrite whatever values could linger.
        while slow < len(nums):
            nums[slow]  = 0
            slow       += 1
