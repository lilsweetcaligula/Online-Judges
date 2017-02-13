#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main(void)
{
    int n; 
    scanf("%d",&n);
        
    const char SPRITE = '#';
    int i = 0, j = 0, k = 0;
    
    for (i = n - 1; i >= 0; --i) {
        for (j = 0; j < i; ++j) putchar(' ');
        for (k = j; k < n; ++k) putchar(SPRITE);
        putchar('\n');
    }
    
    return 0;
}
