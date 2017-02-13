class Solution(object):
    def generatePrefixes(self, s):
        return tuple(s[:end + 1] for end in reversed(range(len(s))))
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefixes = []
        
        for s in strs:
            prefixes.extend(self.generatePrefixes(s))
            
        prefixes = sorted(prefixes)
        count    = 0
        longest  = ''
        
        for index in range(len(prefixes)):
            if index > 0 and prefixes[index - 1] != prefixes[index]:
                count = 1
            else:
                count += 1
                
            if count == len(strs):
                if len(prefixes[index]) > len(longest):
                    longest = prefixes[index]
                    
        return longest
