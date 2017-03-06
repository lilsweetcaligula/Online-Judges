# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/remove-linked-list-elements
@Language: Python
@Datetime: 17-02-15 20:05
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        dummy      = ListNode(0)
        dummy.next = head
        slow       = dummy
        fast       = dummy.next
        
        while fast != None:
            if fast.val != val:
                slow.next = fast
                slow      = slow.next
            fast = fast.next
        
        slow.next = None
            
        return dummy.next