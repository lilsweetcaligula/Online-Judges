#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <ctype.h>
#include <stdio.h>

int main(void) 
{    
    const int ALPHA_LENGTH = 'z' - 'a' + 1;
    
    // Initialize a hash table.
    int table[UCHAR_MAX] = { 0 };
    
    // Collect user input.
    char c         = '\0';
    int alphacount = ALPHA_LENGTH;
    size_t bucket  = 0;
    
    while ((c = getchar()) != '\n' && c != EOF) 
    {
        // Check input against the hash table.    
        c      = tolower(c);
        bucket = (unsigned char)c;
        
        if (isalpha(c) && !table[bucket]) {
            table[bucket] = 1;
            --alphacount;
        }
    }
    
    if (alphacount < 1) puts("pangram");
    else puts("not pangram");
    
    return 0;
}
