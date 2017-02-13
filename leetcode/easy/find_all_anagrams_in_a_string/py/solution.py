class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        import collections
    
        result = []
    
        c1 = collections.Counter(p)
        c2 = collections.Counter(s[:len(p)])
    
        for index in range(len(p), len(s) + 1):
            for letter in c2:
                if c1[letter] != c2[letter]:
                    break
            else:
                result.append(index - len(p))
            
            if index < len(s):
                c2[s[index]]          += 1
                c2[s[index - len(p)]] -= 1
    
        return result
