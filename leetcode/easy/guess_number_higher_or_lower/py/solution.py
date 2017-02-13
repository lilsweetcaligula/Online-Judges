# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n, lo=0):
        """
        :type n: int
        :rtype: int
        """
        if lo >= n:
            return n
            
        if guess(n) == 0:
            return n
    
        x      = lo + (n - lo) // 2
        compar = guess(x)
            
        if compar < 0:
            return self.guessNumber(x, lo)
                
        elif compar > 0:
            return self.guessNumber(n, x)
                
        return x
