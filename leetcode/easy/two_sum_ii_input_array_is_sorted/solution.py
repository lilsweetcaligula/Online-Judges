class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, a in enumerate(numbers):
            b   = target - a
                
            lo  = i + 1
            hi  = len(numbers)
                
            while lo < hi:
                mid = lo + (hi - lo) // 2
                    
                if numbers[mid] < b:
                    lo = mid + 1
                        
                elif numbers[mid] > b:
                    hi = mid
                        
                else:
                    return i + 1, mid + 1
                        
        return ()
