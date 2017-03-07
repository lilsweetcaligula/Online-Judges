class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Selection sort.
        
        for i in xrange(len(A)):
            j = min(xrange(i, len(A)), key=lambda x: A[x])
            A[i], A[j] = A[j], A[i]
