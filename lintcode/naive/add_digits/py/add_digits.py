class Solution:
    # @param {int} num a non-negative integer
    # @return {int} one digit
    def addDigits(self, num):
        
        while len(str(num)) > 1:
            num = sum(map(int, str(num)))
            
        return num
