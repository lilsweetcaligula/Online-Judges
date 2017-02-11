class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import itertools
        
        for num, group in itertools.groupby(sorted(nums)):
            count = len(tuple(group))
            
            if count == 1:
                return num
                
        return None
