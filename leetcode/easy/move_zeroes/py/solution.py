#
# We use a slow/fast pointer technique. The fast pointer (index) is running ahead,
# reporting whether the value it is pointing to is a zero value or not. 
#
# If nums[fast] is not a zero value, we copy the value to nums[slow] and increment
# the slow pointer. This way, by the time the fast pointer reaches the end of the
# array we will have all non-zero values maintaining their initial order to the left 
# of the slow pointer.
#
# At this point, some non-zero values to the right of the slow pointer that have
# been priorly copied, can linger. We must walk the slow pointer to the end of the
# array and overwrite all values with 0.
#

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
                nums[slow] = nums[fast]
                slow      += 1
                
            fast += 1
            
        # All non-zero values have been placed to the left of the slow
        # index now at this point. Fill the remainder of the array with
        # zeros to overwrite whatever values could linger.
        while slow < len(nums):
            nums[slow] = 0
            slow      += 1
