class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import itertools
        
        maxcount = 0
        
        for bit, group in itertools.groupby(nums):
            if bit == 1:
                maxcount = max(maxcount, len(tuple(group)))
                
        return maxcount
