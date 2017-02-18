# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/compare-strings
@Language: Python
@Datetime: 17-02-15 15:02
'''

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        import collections
        
        counter1 = collections.Counter(A)
        counter2 = collections.Counter(B)
        
        for c in counter2:
            if counter1[c] < counter2[c]:
                return False
                
        return True
    