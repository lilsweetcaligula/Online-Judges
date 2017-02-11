#
# The functional approach to this problem would be to use a hash set. A set will
# eliminate all duplicates in the array as well as all numbers already present in
# the array via set.difference method. 
#
# First thing we have to do, however, is to pinpoint the range. The problem spec 
# states that the range is defined by the constraint: 1 ≤ a[i] ≤ n (n = size of array)
# This means the lower bound is 1, whereas the upper inclusive bound is the size of 
# array.
#
# It is important to remember that the upper inclusive bound is either the max. value
# in the array or the array's size, whichever is greater. 
#
# Hence our range can be defined as: range(1, 1 + max(len(nums), max(nums)))
#
# Range is converted to set merely to enable the difference method with the set of numbers
# from the array, whereas nums is converted to a set both to eliminate duplicates and allow
# set.difference be called on it. The important caveat is that set.difference must be called
# from the range set instance and not the set of the numbers from the array. The cardinality
# (length) of the range set is by definition greater than or equal to that of the numbers set
# (no duplicates accounted for since there can be no duplicates in a set).
#

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        return list(set(range(1, 1 + max(len(nums), max(nums)))).difference(set(nums)))
