# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/partition-list
@Language: Python
@Datetime: 17-02-15 23:36
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
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        ltdummy = ListNode(0)
        ltnode  = ltdummy
        
        gtdummy = ListNode(0)
        gtnode  = gtdummy
        
        curr    = head
        
        while curr != None:
            if curr.val < x:
                ltnode.next = curr
                ltnode      = ltnode.next
            else:
                gtnode.next = curr
                gtnode      = gtnode.next
                
            curr = curr.next
            
        ltnode.next = gtdummy.next
        gtnode.next = None
        
        return ltdummy.next