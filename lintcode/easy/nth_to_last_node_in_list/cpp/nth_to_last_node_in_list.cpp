/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/nth-to-last-node-in-list
@Language: C++
@Datetime: 17-02-15 23:26
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
     * @param head: The first node of linked list.
     * @param n: An integer.
     * @return: Nth to last node of a singly linked list. 
     */
    ListNode *nthToLast(ListNode *head, int n) 
    {
        if (head == nullptr) {
            return nullptr;
        }
        
        ListNode *slow{ head }, *fast{ head };
        
        while (n-- > 0)
        {
            if (fast->next == nullptr) {
                return slow;
            }
            fast = fast->next;
        }
        
        while (fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }
        
        return slow->next;
    }
};


