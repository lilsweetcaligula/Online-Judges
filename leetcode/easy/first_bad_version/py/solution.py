# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo = 1
        hi = n + 1
        
        while lo < hi:
            ver = lo + (hi - lo) // 2
            
            if isBadVersion(ver):
                hi = ver
            else:
                lo = ver + 1
                
        return lo
