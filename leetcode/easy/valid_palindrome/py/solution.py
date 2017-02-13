class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = ''.join(filter(lambda c: c.isalnum(), map(unicode.lower, s)))
        return chars == chars[::-1]
