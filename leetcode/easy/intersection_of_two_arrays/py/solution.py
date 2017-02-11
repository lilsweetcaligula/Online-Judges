#
# Python provides for an elegant solution of the intersection problem.
# We simply convert both arrays to sets, thus eliminating any duplicates
# in the process, and then call the set.intersection method to have the
# highly optimized library do the job for us. Mission accomplished.
#

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
