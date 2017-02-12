/*
 * The problem of duplicate deletion from a sorted list can be solved
 * with the help of the slow/fast pointer technique.
 *
 * The slow pointer points to the last element, whereas the fast pointer
 * moves ahead and discards the duplicates. Once a new element is found,
 * The "slow" node is linked up to it by altering its next pointer, and
 * the slow pointer moves a step forward.
 *
 * The reason we are not using the dummy technique here as well, is
 * because even if the head node has duplicates, it is still a unique
 * node in its own respect with all the duplicates deleted.
 *
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) 
{
    if (head == NULL) {
        return NULL;
    }
    
    /*
     * The fast pointer must be initialized with the address
     * of the element following the head node. If both slow
     * and fast pointers are initialized to the head node,
     * the value testing will erroneously consider the node
     * being a duplicate of itself and try to free the head
     * node's memory.
     */
    struct ListNode
        *slow = head,
        *fast = head->next,
        *temp = NULL;
        
    while (fast != NULL) {
        if (slow->val != fast->val) {
            /* The new non-duplicate element located, link up
             * the "slow" node and have the slow pointer move
             * a step forward.
             */
            slow->next = fast;
            slow       = slow->next;
            fast       = fast->next;
        } else {
            /* Store away the address of the next node and free
             * the memory occupied by the duplicate node.
             */             
            fast->next = temp;
            free(fast);
            fast       = fast->next;
        }
    }
    
    /* At this point the last "unique" node might still be
     * pointing at its duplicate. Zero out its next pointer.
     */
    slow->next = NULL;
    
    return head;
}
