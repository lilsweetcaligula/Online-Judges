class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        x   = n
        y   = 1
        cnt = 0
    
        while y <= x:
            x   -= y
            y   += 1
            cnt += 1
    
        return cnt
