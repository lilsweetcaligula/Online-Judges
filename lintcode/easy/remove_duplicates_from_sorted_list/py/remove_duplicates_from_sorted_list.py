# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/remove-duplicates-from-sorted-list
@Language: Python
@Datetime: 17-02-15 23:49
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
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        if head == None:
            return None
        
        slow = head
        fast = head.next
        
        while fast != None:
            if fast.val != slow.val:
                slow.next = fast
                slow      = slow.next
                
            fast = fast.next
            
        slow.next = None
        
        return head