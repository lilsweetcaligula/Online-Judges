#
# Another solution involves allocating an array of indices and sorting it.
# This will provide us with a way to traverse characters in the string in
# a sorted order while preserving the original string.
#
# We then use itertools.groupby to group up the duplicates. Each group is
# then traversed, if the length of a group is equal to one, the character
# is unique, however it is not necessarily the first unique character.
#
# In order to find the first unique character, we use the min() function
# to save the smaller index of a unique character. The important caveat
# is that we initialize the "result" variable to the length of the indices
# array (which is equal to the length of the string). This will enable the
# min function to evaluate the smallest index correctly.
#
# If no unique characters were found, the "result" variable will remain
# equal to the length of the indices array. We check for that, if so,
# we return -1 according to the spec. If not, we return the "result"
# variable.
#

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        import itertools
    
        indices = sorted(range(len(s)), key=lambda x: s[x])
        result  = len(indices)
    
        for char, group in itertools.groupby(indices, key=lambda x: s[x]):
            group = tuple(group)
    
            if len(group) == 1:
                result = min(result, group[0])
    
        if result == len(indices):
            return -1
    
        return result
