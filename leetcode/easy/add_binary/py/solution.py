class Solution(object):
    def addBinary(self, left, right):
        """
        :type left:  str
        :type right: str
        :rtype:      str
        """
        BASE     = 2
        carry    = 0
        leftRev  = left.zfill(len(right))[::-1]
        rightRev = right.zfill(len(left))[::-1]
        result   = ''
            
        for leftBit, rightBit in zip(leftRev, rightRev):
            add     = carry + int(leftBit) + int(rightBit)
            result += str(add % BASE)
            carry   = add // BASE
                
        if carry > 0:
            result += str(carry)
                
        return result[::-1]
