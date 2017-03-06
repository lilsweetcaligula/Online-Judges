# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/convert-sorted-list-to-balanced-bst
@Language: Python
@Datetime: 17-02-16 16:14
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head, end=None):
        if head == None:
            return None
              
        slow = head
        fast = head
        prev = slow
            
        while fast != None and fast.next != None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
                    
        prev.next = None
    
        mid   = slow
        left  = head if mid != head else None
        right = mid.next
            
        root       = TreeNode(mid.val)
        root.left  = self.sortedListToBST(left)
        root.right = self.sortedListToBST(right)
            
        return root