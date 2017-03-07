class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Bubble sort.
    
        wasSwapped = False
        
        for i in xrange(len(A)):
            for j in xrange(i, len(A)):
                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
                    wasSwapped = True
                    
            if not wasSwapped:
                break
