# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/copy-list-with-random-pointer
@Language: Python
@Datetime: 17-02-16 19:33
'''

# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        node = head
        
        # Jam a copy of each node between
        # itself and its next node.
        
        while node != None:
            dupc        = RandomListNode(node.label)
            dupc.next   = node.next
            dupc.random = None
            
            node.next   = dupc
            node        = dupc.next
            
        dummy = ListNode(0)
        dest  = dummy
        node  = head
        
        while node != None:
            dupc        = node.next
            dupc.random = node.random.next if node.random else None
            dest.next   = dupc
            dest        = dest.next
            
            # Jump to the next source node.
            
            node = node.next.next
            
            # No need to worry about going off-rails here.
            # At this point, the list is guaranteed to have
            # an even number of nodes due to each node 
            # having a copy. The list now has 2*n nodes, 
            # where n is the original number of nodes.
            
        return dummy.next