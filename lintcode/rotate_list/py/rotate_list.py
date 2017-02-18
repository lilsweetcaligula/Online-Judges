# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/rotate-list
@Language: Python
@Datetime: 17-02-16 15:41
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head: the list
    # @param k: rotate to the right k places
    # @return: the list after rotation
    def rotateRight(self, head, k):
        if head == None:
            return None
        
        if k == 0:
            return head
    
        dummy = ListNode(0)
        dummy.next = head
            
        slow = dummy
        fast = dummy
            
        while k > 0:
            if fast.next == None:
                fast = dummy.next
            else:
                fast = fast.next
            k -= 1
                
        while fast.next != None:
            slow = slow.next
            fast = fast.next
                
        newHead   = slow.next
        slow.next = None
        fast.next = dummy.next
            
        return newHead