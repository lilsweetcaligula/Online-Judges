class Solution(object):
    def productExceptSelf(self, L):
        """
        :type L: List[int]
        :rtype:  List[int]
        """
        leftprd  = []
        rightprd = []
        left     = 1
        right    = 1
    
        for i in range(len(L)):
            left  *= L[i]
            right *= L[len(L) - i - 1]
    
            leftprd.append(left)
            rightprd.append(right)
    
        rightprd = rightprd[::-1]
        result   = []
    
        for i in range(len(L)):
            if i > 0:
                x = leftprd[i - 1]
            else:
                x = 1
    
            if i + 1 < len(L):
                y = rightprd[i + 1]
            else:
                y = 1
    
            result.append(x * y)
    
        return result
