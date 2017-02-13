class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign    = 1 if x >= 0 else -1
        reverse = sign * int(str(abs(x))[::-1])
        
        if not -(2 ** 31) < reverse < 2 ** 31:
            return 0
            
        return reverse
