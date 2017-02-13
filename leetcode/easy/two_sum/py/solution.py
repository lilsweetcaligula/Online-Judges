class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = sorted(range(len(numbers)), key=lambda x: numbers[x])
        
        for _, i in enumerate(indices):
            a  = numbers[i]
            b  = target - a
                
            lo = 0
            hi = len(indices)
                
            while lo < hi:
                mid = lo + (hi - lo) // 2
                    
                if numbers[indices[mid]] < b:
                    lo = mid + 1
                            
                elif numbers[indices[mid]] > b:
                    hi = mid
                            
                else:
                    return i, indices[mid]
    
        return ()
