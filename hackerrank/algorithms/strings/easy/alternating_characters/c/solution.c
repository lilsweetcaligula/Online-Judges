#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

int main(void) 
{
    int testcount = 0;
    char c = '\0';
    
    while ((c = getchar()) && isdigit(c)) {
        testcount = testcount * 10 + c - '0';
    }
    
    char curr = '\0', prev = '\0';
    
    for (int i = 0; i < testcount; ++i) 
    {
        curr = '\0', prev = '\0';
        int count = 0;
        
        while ((curr = getchar()) != '\n' && curr != EOF) {
            if (curr == prev) {
                ++count;
            }
            prev = curr;
        }
        
        printf("%d\n", count);
    }
    
    return 0;
}
