/*
@Copyright:LintCode
@Author:   lilsweetcaligula
@Problem:  http://www.lintcode.com/problem/add-two-numbers
@Language: C++
@Datetime: 17-02-15 20:26
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    /**
     * @param l1: the first list
     * @param l2: the second list
     * @return: the sum list of l1 and l2 
     */
    ListNode *addLists(ListNode *l1, ListNode *l2) noexcept(false)
    {
        static const int BASE{ 10 };
        ListNode dummy{ 0 }, *dest{ &dummy };
        int carry{ 0 };
        
        while (l1 != nullptr || l2 != nullptr)
        {
            const auto a   = l1 ? l1->val : 0;
            const auto b   = l2 ? l2->val : 0;
            const auto sum = a + b + carry;
            
            carry      = sum / BASE;
            dest->next = new ListNode{ sum % BASE };
            dest       = dest->next;
            
            if (l1 != nullptr) {
                l1 = l1->next;
            }
            
            if (l2 != nullptr) {
                l2 = l2->next;
            }
        }
        
        if (carry) {
            dest->next = new ListNode{ carry };
        }
        
        return dummy.next;
    }
};