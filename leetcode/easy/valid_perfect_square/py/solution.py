class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        import math
    
        if num <= 0:
            return False
    
        eps = 1e-12
        hi  = num
        lo  = 0
            
        while lo <= hi:
            x = lo + (hi - lo) / 2.0
            y = x * x
                
            if abs(num - y) < eps:
                return abs(round(x) - x) < eps
            elif y > num:
                hi = x
            else:
                lo = x
                    
        return False

            
            
