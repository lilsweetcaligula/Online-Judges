# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/merge-two-sorted-lists
@Language: Python
@Datetime: 17-02-15 21:56
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
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        dest  = dummy
        
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                dest.next = l2
                l2        = l2.next
            else:
                dest.next = l1
                l1        = l1.next
                
            dest = dest.next
            
        while l1 != None:
            dest.next = l1
            l1        = l1.next
            dest      = dest.next
        
        while l2 != None:
            dest.next = l2
            l2        = l2.next
            dest      = dest.next
        
        return dummy.next