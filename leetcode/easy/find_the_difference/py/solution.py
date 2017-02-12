class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections
        import itertools
        
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
    
        for char in set(itertools.chain(s, t)):
            if c1[char] != c2[char]:
                return char
                
        return None
