class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ordered = sorted(nums)
    
        for index, value in enumerate(range(ordered[-1] + 1)):
            if value != ordered[index]:
                return value
                
        return value + 1
