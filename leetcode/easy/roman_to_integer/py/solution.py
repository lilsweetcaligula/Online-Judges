class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        LOOKUP = {
            'I': 1,    'i': 1,
            'V': 5,    'v': 5,
            'X': 10,   'x': 10,
            'L': 50,   'l': 50,
            'C': 100,  'c': 100,
            'D': 500,  'd': 500,
            'M': 1000, 'm': 1000
        }
        
        value = 0
    
        for pos in range(len(s)):
            first = LOOKUP[s[pos]]
            
            if pos + 1 != len(s):
                second = LOOKUP[s[pos + 1]]
                
                if first < second:
                    value -= first
                else:
                    value += first
                    
            else:
                value += first
                
        return value
        
