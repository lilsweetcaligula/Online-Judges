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

char findTheDifference(char* s, char* t) 
{
    const size_t slen = strlen(s);
    const size_t tlen = strlen(t);
    
    qsort(s, slen, sizeof(*s), charCompare);
    qsort(t, tlen, sizeof(*t), charCompare);
    
    const char *ps = s;
    const char *pt = t;
    
    while (*ps && *pt && *ps == *pt) {
        ++ps; ++pt;
    }
    
    return slen > tlen ? *ps : *pt;
}
