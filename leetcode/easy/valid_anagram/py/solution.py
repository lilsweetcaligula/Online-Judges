#
# Anagram definition:
#   https://en.wikipedia.org/wiki/Anagram
#
# Classic solution to the anagram problem. Sort both strings
# and check if they are equal.
#
# Time complexity depends on the sorting algorithm
# but we can have O(n log n) at best.
#

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
