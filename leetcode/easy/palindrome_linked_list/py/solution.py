# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        values = []        
        node   = head
        
        while node != None:
            values.append(node.val)
            node = node.next
            
        return values == values[::-1]
