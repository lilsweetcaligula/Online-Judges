# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/add-binary
@Language: Python
@Datetime: 17-02-15 14:35
'''

class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        def xor(a, b):
            import operator
                
            left  = map(int, a.zfill(len(b)))
            right = map(int, b.zfill(len(a)))
                
            return ''.join(str(bit) for bit in map(operator.xor, left, right))
            
        def and_(a, b):
            import operator
                
            left  = map(int, a.zfill(len(b)))
            right = map(int, b.zfill(len(a)))
                
            return ''.join(str(bit) for bit in map(operator.and_, left, right))
                
        def lsh(a, b):
            return a + '0' * int(b)
            
        def helper(a, b):
            if len(b) == 0:
                return a if len(a) > 0 else '0'
                
            total = xor(a, b)
            carry = lsh(and_(a, b), 1)
                    
            return helper(total.lstrip('0'), carry.lstrip('0'))
            
        return helper(a, b)