class Solution(object):
    def trailingZeroes(self, n):
        count = 0
        div   = 5
    
        while n // div > 0:
            count += n // div
            div   *= 5
    
        return count
