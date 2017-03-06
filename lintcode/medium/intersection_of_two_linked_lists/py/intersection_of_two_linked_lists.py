# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/intersection-of-two-linked-lists
@Language: Python
@Datetime: 17-02-16 16:50
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None
            
        first = headA
        last  = headA
        
        while last.next != None:
            last = last.next
            
        # Temporarily make a cycle. We will remove
        # the cycle once we check the status of the
        # intersection.
        
        last.next = first
        
        slow = headB
        fast = headB
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                break
                
        if fast == slow:
            # There exists an intersection between
            # the two lists.
            
            slow = headB
            
            while fast != slow:
                slow = slow.next
                fast = fast.next
                
            # The intersection node is now the one
            # pointed to by the "slow" pointer. We
            # now restore the original structure of
            # the lists.
            
            last.next = None
            
            return slow
            
        # There exists no intersection between
        # the two lists. Restore the original
        # structure and return.
        
        last.next = None
        
        return None
            