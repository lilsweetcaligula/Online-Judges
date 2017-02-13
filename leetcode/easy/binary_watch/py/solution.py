class Solution(object):
    def readBinaryWatch(self, n):
        """
        :type n: int
        :rtype:  List[str]
        """
        
        def helper(bitcnt, n, curval=0, vals=None):
            if n == 0:
                if curval != 0:
                    vals.append(curval)
                return [0]
    
            if vals == None:
                vals = []
    
            lsh = 0
    
            while (lsh < bitcnt) and ((curval & (1 << lsh)) == 0):
                helper(bitcnt, n - 1, curval | (1 << lsh), vals)
                lsh += 1
    
            return vals
        
        HRS_BIT_COUNT = 4
        MIN_BIT_COUNT = 6
    
        MAX_HRS       = 11
        MAX_MIN       = 59
    
        timebits = helper(HRS_BIT_COUNT + MIN_BIT_COUNT, n)
        result   = []
    
        for value in timebits:
            hrs  = value >> MIN_BIT_COUNT
            mins = value & ((1 << MIN_BIT_COUNT) - 1)
    
            if 0 <= hrs <= MAX_HRS and 0 <= mins <= MAX_MIN:
                result.append('{}:{:02}'.format(hrs, mins))
    
        return result
