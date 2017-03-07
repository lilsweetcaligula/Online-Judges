class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        if n == 1:
            return 0
            
        prev = 0
        curr = 1
        i    = 0
        
        while i < n - 2:
            prev, curr = curr, prev + curr            
            i += 1

        return curr
