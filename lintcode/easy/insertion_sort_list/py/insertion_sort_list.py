# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/insertion-sort-list
@Language: Python
@Datetime: 17-02-15 21:47
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
    @return: The head of linked list.
    """ 
    def insertionSortList(self, head):
        dummy = ListNode(0)
        src   = head
        
        while src != None:
            if src.next != None and src.val > src.next.val:
                break
            
            src = src.next
        else:
            return head
        
        src = head
        
        while src != None:
            nxt = src.next
            dst = dummy
            
            while dst.next != None and dst.next.val < src.val:
                dst = dst.next
            
            src.next = dst.next
            dst.next = src
            src      = nxt
            
        return dummy.next