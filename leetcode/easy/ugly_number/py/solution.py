class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
    
        bad_factors = (2, 3, 5)
    
        stack = [num]
    
        while len(stack) > 0:
            x = stack.pop()
    
            if x == 1:
                return True
            else:
                for bad_factor in bad_factors:
                    if x % bad_factor == 0:
                        y = x // bad_factor
                        stack.append(y)
    
        return False
