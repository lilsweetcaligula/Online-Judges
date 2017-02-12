class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        import collections
        
        c1 = collections.Counter(ransomNote)
        c2 = collections.Counter(magazine)
        
        for char in c1:
            if c2[char] < c1[char]:
                return False
                
        return True
