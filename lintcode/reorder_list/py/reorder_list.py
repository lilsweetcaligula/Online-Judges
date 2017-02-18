# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/reorder-list
@Language: Python
@Datetime: 17-02-16 20:39
'''

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr != None:
            temp      = curr.next
            curr.next = prev
            prev      = curr
            curr      = temp
            
        return prev
    
    """
    @param head: The first node of the linked list.
    @return: nothing
    """
    def reorderList(self, head):
        if head == None:
            return None
            
        # Find the middle node of the list.
            
        slow = head
        fast = head
            
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
                
        mid = slow
                
        # Push the second half of the list
        # onto the stack.
            
        stack = []    
                
        while slow != None:
            stack.append(slow)
            slow = slow.next
                
        # Build a list according to the spec.    
            
        dummy = ListNode(0)
        dest  = dummy
        lnode = head
            
        while len(stack) > 0:
            temp       = lnode.next
        
            rnode      = stack.pop()
            lnode.next = rnode
            dest.next  = lnode
            dest       = dest.next.next
        
            lnode      = temp
        
        dest.next = None
                
        return dummy.next