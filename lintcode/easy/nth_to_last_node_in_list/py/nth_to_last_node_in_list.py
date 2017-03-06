# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/nth-to-last-node-in-list
@Language: Python
@Datetime: 17-02-15 23:23
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
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        if head == None:
            return None
            
        slow = head
        fast = head
        
        while n > 0:
            if fast.next == None:
                return slow
                
            fast = fast.next
            n   -= 1
            
        while fast.next != None:
            slow = slow.next
            fast = fast.next
            
        return slow.next