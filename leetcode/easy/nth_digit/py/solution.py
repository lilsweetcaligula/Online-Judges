class Solution(object):
    def findNthDigit(self, x):
        """
        :type x: int
        :rtype:  int
        """
        import math
    
        curtotcnt = 0
        nxttotcnt = 10
        coeff     = 1
    
        while nxttotcnt < x:            
            curtotcnt  = nxttotcnt
            nxttotcnt  = curtotcnt + (1 + coeff) * 9 * 10 ** coeff
            coeff     += 1
    
        if coeff > 1:
            rngbegin = 10 ** (coeff - 1)
        else:
            rngbegin = 0
        
        digoffset = x - curtotcnt
        valoffset = digoffset // coeff
        value     = rngbegin + valoffset
    
        return int(str(value)[digoffset % coeff])
