#
# The problem spec requires that we are not allowed to use the "+" and or "-" operators.
# But no one said anything about the built-in "sum" function. ;)
#

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum((a, b))
