#
# The functional approach to solving this problem could be as follows.
# Filter out all non-vowels in the source string while maintaining
# their relative order. 
#
# Then construct a string placing the replacement fields '{}' where a
# vowel was, or copying the character if the character is not a vowel.
#
# We then call str.format method on the constructed string, unpack
# the vowels from the original string and reverse them to use as
# arguments.
#

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS    = frozenset('aeouiAEOUI')
        srcVowels = filter(lambda c: c in VOWELS, s)
        
        return ''.join(c if c not in VOWELS else '{}' for c in s).format(*tuple(srcVowels)[::-1])
