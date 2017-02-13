class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        indices = sorted(range(len(nums)), key=lambda x: nums[x])
        
        for i in range(1, len(indices)):
            if (abs(indices[i] - indices[i - 1]) <= k 
                and nums[indices[i]] == nums[indices[i - 1]]):
                return True
                
        return False
