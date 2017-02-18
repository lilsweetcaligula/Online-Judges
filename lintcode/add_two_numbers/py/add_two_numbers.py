# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/add-two-numbers
@Language: Python
@Datetime: 17-02-15 20:17
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2 
    def addLists(self, l1, l2):
        base  = 10
        dummy = ListNode(0)
        dest  = dummy
        carry = 0
        
        while l1 != None or l2 != None:
            if l1 == None:
                a = 0
            else:
                a  = l1.val
                l1 = l1.next
                
            if l2 == None:
                b = 0
            else:
                b  = l2.val
                l2 = l2.next
                
            total = a + b + carry
            carry = total // base
            
            dest.next = ListNode(total % base)
            dest      = dest.next
            
        if carry:
            dest.next = ListNode(carry)
            
        return dummy.next