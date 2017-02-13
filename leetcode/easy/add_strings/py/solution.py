class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = ''
        carry  = 0
        
        digs1  = num1.zfill(len(num2))[::-1]
        digs2  = num2.zfill(len(num1))[::-1]
    
        for dig1, dig2 in zip(digs1, digs2):
            add     = carry + sum(map(int, (dig1, dig2)))
            resdig  = str(add % 10)
            carry   = add // 10
                
            result += resdig
                
        if carry > 0:
            result += str(carry)
                
        return result[::-1]
