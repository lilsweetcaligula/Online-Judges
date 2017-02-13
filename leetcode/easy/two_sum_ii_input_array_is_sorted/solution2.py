class Solution(object):
    @staticmethod
    def bsearch(L, x, lo=None, hi=None):
        if lo == None:
            lo = 0
        
        if hi == None:
            hi = len(L)

        begin = lo
        end   = hi
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if L[mid] >= x:
                hi = mid
            elif L[mid] < x:
                lo = mid + 1
             
        if begin <= lo < end and L[lo] == x:
            return lo

        return -1
    
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, x in enumerate(numbers):
            y = target - x
            j = Solution.bsearch(numbers, y, lo=i + 1)
            
            if i < j < len(numbers):
                return i + 1, j + 1
                        
        return ()
