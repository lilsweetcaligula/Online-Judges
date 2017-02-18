/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/partition-list
@Language: C++
@Datetime: 17-02-15 23:43
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
     * @param x: an integer
     * @return: a ListNode 
     */
    ListNode *partition(ListNode *head, int x) 
    {
        auto ltdummy = ListNode{ 0 };
        auto ltnode  = &ltdummy;
        
        auto gtdummy = ListNode{ 0 };
        auto gtnode  = &gtdummy;
        
        auto curr    = head;
        
        while (curr != nullptr)
        {
            if (curr->val < x) {
                ltnode->next = curr;
                ltnode       = ltnode->next;
            } else {
                gtnode->next = curr;
                gtnode       = gtnode->next;
            }
            
            curr = curr->next;
        }
        
        ltnode->next = gtdummy.next;
        gtnode->next = nullptr;
        
        return ltdummy.next;
    }
};


