#
# The lazybones' approach. In order to eliminate duplicates, conver the array
# to a set. Sort the values in the set and assign the sorted array back to "nums".
# The [:] subscript operator is important in emulating assignment by reference.
# In reality, given no arguments as it is shown in the code, it simply copies 
# the values and alters its length in accordance with the number of values copied 
# from the source.
#
# Returning the length of the array as required by the problem statement.
#
# O(n) time with the possibility of degrading to O(n^2) due to possible collisions
# that may arise in the set. O(n) space to hold the set and the temporary buffer
# for sorted values.
#

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = sorted(set(nums))
        return len(nums)
