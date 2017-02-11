class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        return list(set(range(1, 1 + max(len(nums), max(nums)))).difference(set(nums)))
