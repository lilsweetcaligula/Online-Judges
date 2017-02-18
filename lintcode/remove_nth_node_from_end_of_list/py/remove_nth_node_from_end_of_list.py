# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/remove-nth-node-from-end-of-list
@Language: Python
@Datetime: 17-02-16 00:00
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if head == None:
            return None
        
        dummy = ListNode(0, head)
        slow  = dummy
        fast  = dummy
        
        while n > 0:
            fast = fast.next
            n   -= 1
            
        while fast.next != None:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return dummy.next