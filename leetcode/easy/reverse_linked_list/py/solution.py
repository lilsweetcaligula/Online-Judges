#
# Recursive solution for the linked list reversal problem. The trick to
# get it "right" is to add the "prev" argument to the function, which
# represents the previous node according to the initial order of the linked
# list.
#
# The pointer to the ex-previous node will provide a viable piece information
# for us in order to link up the new head to its predecessor.
#

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head, prev=None):
        """
        :type head: ListNode
        :type prev: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        
        temp      = head.next
        head.next = prev
        
        if temp:
            return self.reverseList(temp, head)
        
        return head
