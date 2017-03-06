# coding:utf-8
'''
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/swap-two-nodes-in-linked-list
@Language: Python
@Datetime: 17-02-17 09:31
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head, a ListNode
    # @oaram {int} v1 an integer
    # @param {int} v2 an integer
    # @return {ListNode} a new head of singly-linked list
    def swapNodes(self, head, v1, v2):
        dummy      = ListNode(0)
        dummy.next = head
        node       = dummy
        n1         = None
        n2         = None
            
        while node.next != None:
            if node.next.val == v1:
                n1 = node
            elif node.next.val == v2:
                n2 = node
            node = node.next
    
        if n1 != None and n2 != None:
            if n1.next == n2 or n2.next == n1:
                                                        
                # Special case. The target nodes
                # are neighboring nodes.
    
                if n1.next == n2:
    
                    # v1 goes first in the list.
    
                    left  = n1
                    right = n2
                    
                elif n2.next == n1:
    
                    # v2 goes first in the list.
    
                    left  = n2
                    right = n1
                
                ltarget = left.next
                rtarget = right.next
    
                temp         = rtarget.next
                rtarget.next = ltarget
                ltarget.next = temp
                left.next    = rtarget
    
            else:
                nxt1 = n1.next.next
                nxt2 = n2.next.next
                    
                tmp1 = n1.next
                    
                n1.next      = n2.next
                n1.next.next = nxt1
                    
                n2.next      = tmp1
                n2.next.next = nxt2
                
        return dummy.next