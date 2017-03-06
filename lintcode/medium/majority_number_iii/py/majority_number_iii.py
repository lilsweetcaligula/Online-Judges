class Solution:
    """
    @param nums: A list of integers
    @param k: As described
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        import collections
        
        ratio   = 1.0 / k * len(nums)
        counter = collections.Counter(nums)
        
        for num in counter:
            count = counter[num]
        
            if count > ratio:
                return num
                
        return None
