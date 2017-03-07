class Solution:
    # @param {int} num a non-negative integer
    # @return {int} one digit
    def addDigits(self, num):
        while num > 9:
            nxt = 0
            
            while num > 0:
                nxt  += num % 10
                num //= 10
                
            num = nxt
                
        return num
