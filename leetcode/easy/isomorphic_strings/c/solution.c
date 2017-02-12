#include <limits.h>

bool isIsomorphic(char* s, char* t)
{
    int slookup[UCHAR_MAX] = { 0 };
    int tlookup[UCHAR_MAX] = { 0 };
    
    while (*s != '\0' && *t != '\0') {
        if (!slookup[*s] && !tlookup[*t]) {
            slookup[*s] = *t; 
            tlookup[*t] = *s;
        } else if (slookup[*s] != *t) {
            return false;
        }
        ++s; ++t;
    }
    
    return *s == '\0' && *t == '\0';
}
