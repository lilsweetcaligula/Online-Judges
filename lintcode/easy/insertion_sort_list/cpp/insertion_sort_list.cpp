/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/insertion-sort-list
@Language: C++
@Datetime: 17-02-15 23:13
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
     * @return: The head of linked list.
     */
    ListNode *insertionSortList(ListNode *head) 
    {
        ListNode dummy{ 0 }, *src{ head };
            
        while (src != nullptr) {
            if (src->next != nullptr && src->val > src->next->val) {
                break;
            }
            src = src->next;
        }
        
        if (src == nullptr) {
            return head;
        }
            
        src = head;
            
        while (src != nullptr)
        {
            ListNode *next{ src->next };
            ListNode *dest{ &dummy };
            
            while (dest->next != nullptr && src->val > dest->next->val) {
                dest = dest->next;
            }
            
            src->next  = dest->next;
            dest->next = src;
            src        = next;
        }
        
        return dummy.next;
    }
};