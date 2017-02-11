/*
 * In order to find the first unique character, we can use a hash table.
 * We allocate enough slots to accommodate all possible ASCII characters, thus
 * ensuring no collisions and guaranteeing an O(1) access time and O(n) performance
 * for the solution.
 *
 * We save the frequencies of every character of the string on the first pass. On
 * the second pass of the string we query the lookup table and check whether the
 * current character's frequency is equal to one. If it is, we have found the unique
 * character in the string.
 *
 */

#include <limits.h>
#include <stddef.h>

int firstUniqChar(char* s) 
{
    size_t lookup[UCHAR_MAX] = { 0 };
    
    for (const char *pc = s; *pc != '\0'; ++pc) {
        ++lookup[*pc];
    }
    
    for (const char *pc = s; *pc != '\0'; ++pc) {
        if (lookup[*pc] == 1) {
            return (pc - s);
        }
    }
    
    return -1;
}
