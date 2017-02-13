class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        
        counter = collections.Counter(nums)
        
        for num, count in counter.items():
            if count > len(nums) // 2:
                return num
        
        return None
