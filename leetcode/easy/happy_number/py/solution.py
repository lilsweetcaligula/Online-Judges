class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        x       = n
        visited = set()
        
        while x != 1:
            if x in visited:
                return False
            else:
                visited.add(x)
                x = sum(map(lambda x: x ** 2, map(int, str(x))))
                
        return True
