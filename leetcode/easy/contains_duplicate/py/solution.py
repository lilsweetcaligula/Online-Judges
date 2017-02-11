#
# An interesting approach to the problem of finding a duplicate
# in an array can be the following.
#
# We use a set to rid the array of duplicates and compare its
# length to the original length of the array. If the original
# array happens to have a greater length, then we definitely had
# the duplicates.
#

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) > len(set(nums))
