class Solution:
    """
    @param seq    : A sorted (x1 <= x2 ... <= xN) linearly sequential iterable (i.e. array)
    @param target : Item to be on a lookout for.
    @param lo     : Lower bound to start the search at.
    @param hi     : Upper exclusive bound to terminate the search at.
    @param key    : The key accessor function. Identity function by default.
    """
    @staticmethod
    def binarySearch(seq, target, lo=None, hi=None, key=None):
        if lo == None:
            lo = 0
            
        if hi == None:
            hi = len(seq)
            
        if key == None:
            key = lambda x: x
            
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if target > key(seq[mid]):
                lo = mid + 1
            elif target < key(seq[mid]):
                hi = mid
            else:
                return mid
                
        return -1
    
    """
    @param numbers : An array of Integer
    @param target  : target = numbers[index1] + numbers[index2]
    @return        : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        indices = sorted(range(len(numbers)), key=lambda x: numbers[x])
        
        for i in range(len(indices)):
            j = -1

            while True:
                j = Solution.binarySearch(
                    indices, target - numbers[indices[i]],
                    lo=j + 1, key=lambda x: numbers[x])
                                
                if 0 <= j < len(indices):
                    if j != i:
                        return sorted([1 + indices[i], 1 + indices[j]])
                else:
                    break
                
        return [-1, -1]
