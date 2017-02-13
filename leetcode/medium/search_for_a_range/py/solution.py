class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo = 0
        hi = len(nums)
    
        while lo < hi:
            mid = lo + (hi - lo) // 2
    
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1
        
        if lo == len(nums) or nums[lo] != target:
            return [-1, -1]
    
        begin = lo
        hi    = len(nums)
    
        while lo < hi:
            mid = lo + (hi - lo) // 2
    
            if nums[mid] > target:
                hi = mid
            else:
                lo = mid + 1
    
        end = lo - 1
        
        return [begin, end]
