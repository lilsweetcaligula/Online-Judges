class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        
        counter   = collections.Counter(s)
        pairCount = 0
        
        for letter in counter:
            frequency  = counter[letter]
            pairCount += frequency // 2
        
        if 2 * pairCount < len(s):
            return 2 * pairCount + 1
        
        return 2 * pairCount
