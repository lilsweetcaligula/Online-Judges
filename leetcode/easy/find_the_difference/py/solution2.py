class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import itertools
        
        for c1, c2 in itertools.izip_longest(sorted(s), sorted(t)):        
            c1 = c1 if c1 else ''
            c2 = c2 if c2 else ''
            
            if c1 != c2:
                if len(s) > len(t):
                    return c1
                else:
                    return c2
                    
        return None
