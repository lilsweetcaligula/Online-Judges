# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/swap-nodes-in-pairs
@Language: Python
@Datetime: 17-02-16 00:32
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None:
            return None
            
        dummy  = ListNode(0)
        dummy.next = head
    
        prev   = dummy
        first  = dummy
        second = None
            
        while first.next != None and first.next.next != None:
            first       = first.next
            second      = first.next
    
            temp        = second.next
                
            second.next = first
            first.next  = temp
                
            prev.next   = second
            prev        = first
                
        return dummy.next