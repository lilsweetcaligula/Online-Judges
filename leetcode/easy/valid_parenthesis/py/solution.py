class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        LPARENS = {
            '(': ')', '{': '}', '[': ']'   
        }
        
        RPARENS = {
            ')': '(', '}': '{', ']': '['
        }
        
        stack = []
        
        for c in s:            
            if c in LPARENS:
                stack.append(c)
                
            elif c in RPARENS:
                if len(stack) == 0:
                    return False
                    
                t = stack.pop()
                
                if RPARENS[c] != t:
                    return False
                    
        return len(stack) == 0
