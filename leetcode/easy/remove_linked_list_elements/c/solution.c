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
        *temp = NULL,
        dummy = { .next = head },
        *slow = &dummy,
        *fast = (&dummy)->next;
        
    while (fast != NULL)
    {
        if (fast->val != val) {
            slow->next = fast;
            slow       = slow->next;
            fast       = fast->next;
        } else {
            // We found the node containing the target value.
            // De-allocate the node. Store away the pointer to
            // the next node. Otherwise, it will be unavailable
            // to us once we free the target node's memory.
            temp = fast->next;
            free(fast); fast = temp;
        }
    }
    slow->next = NULL;
    
    return dummy.next;
}
