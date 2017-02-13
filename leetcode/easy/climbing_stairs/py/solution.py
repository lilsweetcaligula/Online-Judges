class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev = 1
        curr = 1
        
        for i in range(1, n):
            prev, curr = curr, prev + curr
            
        return curr
