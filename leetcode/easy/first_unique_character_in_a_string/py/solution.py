#
# In order to find the first unique character in a string in Python,
# we can use the collections.Counter class to count the frequencies
# of characters in the string. Access time at the worst can be O(n),
# at best O(1), thus resulting in solution performance varying from
# O(n^2) to O(n). However, it is important to note that the O(n) access
# time for a collections.Counter object is highly unlikely.
#
# An optimization could be to pre-allocate a buffer with enough slots to
# accommodate all ASCII characters, which will ensure no collisions. 
# This would prove quite costly memory-wise for non-ASCII charsets, however.
#

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        
        lookup = collections.Counter(s)
        
        for index, char in enumerate(s):
            count = lookup[char]
            
            if count == 1:
                return index
                
        return -1
