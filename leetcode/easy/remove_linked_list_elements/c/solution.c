/*
 * The good ol'slow/fast pointer/index approach coupled with the dummy
 * technique for linked lists. Simply allocate a dummy (preferrably on
 * the stack) and have its next pointer point to the head node. This
 * will save us an extra case when the head node value is equal to the
 * target value.
 *
 * O(n) time, O(1) space.
 */

#include <stddef.h>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeElements(struct ListNode* head, int val) 
{
    struct ListNode
        dummy = { .next = head },
        *slow = &dummy,
        *fast = &dummy;
        
    while (fast != NULL) {
        if (fast->next != NULL && fast->next->val == val) {
            fast       = fast->next;   
        } else {
            slow->next = fast->next;
            fast       = fast->next;
            slow       = slow->next;
        }
    }
    
    return dummy.next;
}
