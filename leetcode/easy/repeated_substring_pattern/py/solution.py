class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        count = 2
        
        while count <= len(s):
            chunk = s[:len(s) // count]
            
            if chunk * count == s:
                return True
                
            count += 1
            
        return False
