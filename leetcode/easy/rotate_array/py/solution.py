class Solution(object):

    # Right rotation.
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k        = k % len(nums)
        nums[:]  = reversed(nums)
        nums[k:] = reversed(nums[k:])
        nums[:k] = reversed(nums[:k])
