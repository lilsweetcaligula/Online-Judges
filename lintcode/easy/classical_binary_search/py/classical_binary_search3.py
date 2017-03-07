class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        lo = 0
        hi = len(A) - 1
        
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            
            if A[mid] > target:
                hi = mid - 1
            elif A[mid] < target:
                lo = mid + 1
            else:
                return mid
                
        return -1
