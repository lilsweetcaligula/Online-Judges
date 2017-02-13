class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = num
        
        while len(str(x)) != 1:
            x = sum(map(int, str(x)))
            
        return x
