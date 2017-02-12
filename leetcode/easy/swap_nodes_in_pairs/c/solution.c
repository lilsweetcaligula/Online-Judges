/*
 * To accomplish node swapping in pairs in a linked list, in this solution,
 * we make use of the dummy technique.
 *
 * As we traverse the linked list, we append pairs of consequent nodes to
 * the tail of the "dummy"-headed linked list.
 *
 * At the end of the traversal the dummy node's next pointer points at the
 * head of our linked list with its nodes swapped in pairs.
 *
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) 
{
    if (head == NULL) {
        return NULL;
    }
    
    struct ListNode
        dummy = { .next = NULL },
        *dest = &dummy,
        *src  = head,
        *next = NULL;
        
    while (src != NULL) 
    {
        // Save the address of the first node in the next pair.
        // If the current node itself has no pair, means we are
        // at the end of the list and there's no next pair.
        //
        next = src->next != NULL ? src->next->next : NULL;
        
        struct ListNode 
            *first  = src,
            *second = src->next;
        
        // Does the current node have a pair? If it does,
        // its pair should come first after the swap.
        // Append to the "dummy"-headed list and move
        // the "dest" pointer to the appended node.
        //
        if (second != NULL) {
            dest->next  = second;
            dest        = dest->next;
        }
        
        // Append the first node that after the swap
        // should come second.
        //
        dest->next  = first;
        dest        = dest->next;
        src         = next;
    }
    
    // The "dummy"-headed list's tail is still pointing
    // at the original last element. Zero its next pointer
    // out.
    //
    dest->next = NULL;
    
    return dummy.next;
}
