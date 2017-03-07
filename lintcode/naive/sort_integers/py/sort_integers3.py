class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Insertion sort.
        
        for i in xrange(len(A)):
            for j in xrange(i, 0, -1):
                if A[j - 1] <= A[j]:
                    break
                else:
                    A[j], A[j - 1] = A[j - 1], A[j]
