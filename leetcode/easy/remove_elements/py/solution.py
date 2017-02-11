#
# Here at Python Solutions Inc. we like to present you with
# ways to get the job done on a lazy sleepless Monday in Seattle.
#
# Use the built-in filter function to filter out the target values.
# This will be an O(n) space. 
#
# Copy the result back to nums. This will be O(2n) time complexity, 
# or simply O(n).
#
# Return the new length of the nums as required by the problem
# statement.
#

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        nums[:] = filter(lambda x: x != val, nums)
        return len(nums)
