# 
# In order to count the number of segments in a string, defined as
# a contiguous sequence of non-space characters, we can use the
# str.split function:
#   https://docs.python.org/3/library/stdtypes.html#str.split
#
# Given no parameters, the string is split on consecutive runs of
# whitespace and produce a list of segments. We simply return
# the length of the list.
#

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
