/*
 * Definition of anagram:
 *  https://en.wikipedia.org/wiki/Anagram
 *
 * An alternative to sorting both strings and comparing them O(n log n),
 * would be using a hash table, thus trading space for faster performance O(n).
 *
 * O(n) performance is guaranteed since the lookup table we pre-allocate
 * has enough slots to accommodate all ASCII characters, thus ensuring
 * that no two different elements will ever be hashed to the same slot.
 *
 * However, prior to allocating the table, we first need to make sure both
 * strings have the same length. If not, they cannot be anagrams by definition.
 *
 * Save the frequency of each character in the table on the pass of the first 
 * string. Traverse the second string and match its every character against
 * the lookup table, decrementing the frequency on the match. If the entry
 * for the given character of the second string is 0, that means we either
 * have a mismatch or a redundant character, hence the strings are not anagrams.
 *
 */

#include <limits.h>
#include <stddef.h>

bool isAnagram(char* s, char* t) 
{
    if (strlen(s) != strlen(t)) {
        return false;
    }
    
    size_t lookup[UCHAR_MAX] = { 0 };
    
    for (const char *pchar = s; *pchar; ++pchar) {
        ++lookup[*pchar]; 
    }

    for (const char *pchar = t; *pchar; ++pchar) {
        if (lookup[*pchar] == 0) {
            return false;
        } else {
            --lookup[*pchar];
        }
    }
    
    return true;
}
