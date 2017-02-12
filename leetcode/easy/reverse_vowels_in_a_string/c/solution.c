/*
 * The procedural solution to the problem of vowel reversal requires
 * to traverse the string with two indices - the first starting at 
 * the beginning of the string and the second starting at the last
 * character.
 *
 * The mission of each index is to locate a vowel. Once one of the
 * indices locates a vowel, the opposite index has to be aligned
 * at the opposite vowel. 
 *
 * Once both indices are aligned on two opposite vowels, they
 * are swapped, and the traversal continues. If there's only
 * one vowel in the string the indices will meet and the
 * traversal will stop.
 *
 */

#include <string.h>

static bool isVowel(int ch) 
{
    static const char *VOWELS = "aeouiAEOUI";
    return strchr(VOWELS, ch) != NULL;
}

char* reverseVowels(char* s) 
{
    char *left  = s;
    char *right = &s[strlen(s)] - 1;
    
    while (left < right)
    {
        if (isVowel(*left) && isVowel(*right)) {
            const char temp = *right;
            *right          = *left;
            *left           = temp;
            ++left; --right;
        } else if (isVowel(*left)) {
            --right;
        } else {
            ++left;
        }
    }
    
    return s;
}
