#
# Here at Python Solutions Inc. we like to present you with
# ways to get the job done on a lazy sleepless Monday in Seattle.
#
# Use filter to filter out target values - O(n) space. Copy the
# result back to nums. O(2n) time complexity, or simply O(n).
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
