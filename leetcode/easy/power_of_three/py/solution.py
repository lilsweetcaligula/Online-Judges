class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math

        if n < 1:
            return False

        base = 3
        eps  = 1e-13 
        log  = math.log(n, base)
    
        if abs(math.ceil(log) - log) < eps:
            log = math.ceil(log)
    
        return math.floor(log) == math.ceil(log)
