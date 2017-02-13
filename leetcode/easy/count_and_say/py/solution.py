class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
            
        while n > 1:
            t   = ''
            cnt = 1
                
            for i in range(len(s)):
                if i + 1 < len(s) and s[i] == s[i + 1]:
                    cnt += 1
                else:
                    t   += str(cnt) + s[i] 
                    cnt  = 1
                        
            s  = t        
            n -= 1
            
        return s
