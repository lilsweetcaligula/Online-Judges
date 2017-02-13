#include <string.h>
#include <ctype.h>

int lengthOfLastWord(char* s) 
{
    const char *end = &s[strlen(s)];
    int count       = 0;
    
    while (end >= s && isspace(*--end)) {
        continue;
    }
    
    while (end >= s && !isspace(*end--)) {
        ++count;
    }
    
    return count;
}
