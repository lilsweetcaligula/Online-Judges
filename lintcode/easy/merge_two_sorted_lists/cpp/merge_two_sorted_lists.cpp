/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/merge-two-sorted-lists
@Language: C++
@Datetime: 17-02-15 23:17
*/

/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param ListNode left is the head of the linked list
     * @param ListNode right is the head of the linked list
     * @return: ListNode head of linked list
     */
    ListNode *mergeTwoLists(ListNode *left, ListNode *right)
    {
        ListNode dummy{ 0 }, *tail{ &dummy };
        
        while (left != nullptr && right != nullptr)
        {
            if (left->val > right->val) {
                tail->next = right;
                right      = right->next;
            } else {
                tail->next = left;
                left       = left->next;
            }
            
            tail = tail->next;
        }
        
        while (left != nullptr) {
            tail->next = left;
            left       = left->next;
            tail       = tail->next;
        }
        
        while (right != nullptr) {
            tail->next = right;
            right      = right->next;
            tail       = tail->next;
        }
        
        return dummy.next;
    }
};