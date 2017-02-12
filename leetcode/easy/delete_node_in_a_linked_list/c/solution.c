/*
 * Given access only to the node to be deleted, the way to "delete" it,
 * would be to shift all nodes to the right of it, left.
 *
 * In other words, we keep going to the right, swappig values. When
 * we reach the penultimate node, we free the last node, and zero out
 * the penultimate's node pointer.
 *
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void deleteNode(struct ListNode* node) {
    struct ListNode
        *curr = node,
        *next = node->next;
    
    while (next != NULL) 
    {
        const int temp = curr->val;
        curr->val      = next->val;
        next->val      = temp;
        
        next           = next->next;
        
        if (next != NULL) {
            curr = curr->next;
        }
    }
    
    free(curr->next); curr->next = NULL;
}
