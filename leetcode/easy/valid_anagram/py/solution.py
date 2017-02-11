#
# Anagram definition:
#   https://en.wikipedia.org/wiki/Anagram
#
# Classic solution to the anagram problem.
# Sort both strings and check if they are equal.
#

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
