class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        import bisect
        
        i = bisect.bisect_left(A, target)
        
        if i < len(A) and A[i] == target:
            return i
            
        return -1
