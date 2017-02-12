class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        import string
        
        return int(bin(num)[2:].translate(string.maketrans('10', '01')), base=2)
