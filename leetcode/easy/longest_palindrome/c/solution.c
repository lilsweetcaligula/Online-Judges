#include <stdlib.h>
#include <string.h>

int charCompare(const void *left, const void *right)
{
    const char leftChar  = *((const char*)left);
    const char rightChar = *((const char*)right);
    
    if (leftChar < rightChar) {
        return -1;
    }
    else if (leftChar > rightChar) {
        return 1;
    }
    
    return 0;
}

int longestPalindrome(char* s)
{
    const size_t length = strlen(s);
    
    qsort(s, length, sizeof(*s), charCompare);
    
    int    pairCount = 0;
    size_t index     = 0;
    
    while (index < length) {
        if (s[index] == s[index - 1]) {
            ++pairCount; ++index;
        }
        ++index;
    }
    
    return (2 * pairCount < length) ? 
        2 * pairCount + 1 : 2 * pairCount;
}
