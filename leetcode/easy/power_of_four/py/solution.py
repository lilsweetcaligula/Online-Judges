class Solution(object):
    def isPowerOfFour(self, x):
        """
        :type num: int
        :rtype: bool
        """
        bits = 1
        
        while bits < x:
            bits <<= 2
            
        return bits == x
