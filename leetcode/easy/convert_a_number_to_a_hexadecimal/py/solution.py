#
# Yeah, we could just use the built-in "hex" function, but where's the challenge in that?
#

class Solution(object):
    def toHex(self, number):
        """
        :type number: int
        :rtype: str
        """
        import ctypes
        
        HEX_LOOKUP = '0123456789abcdef'
        BASE       = 16
        
        result     = ''
        number     = ctypes.c_uint32(number).value
        
        while True:
            result  += HEX_LOOKUP[number % BASE]
            number //= BASE
            
            if number == 0:
                break
            
        return result[::-1]
