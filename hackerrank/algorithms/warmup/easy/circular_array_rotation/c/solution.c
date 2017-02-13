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
    int k; 
    int q; 
    int *a;
    
    scanf("%d %d %d",&n,&k,&q);
    
    a = malloc(sizeof(int) * n);
    k = k % n;
    
    if (!a) {
        return EXIT_FAILURE;
    }
    
    for (int a_i = 0; a_i < n; a_i++){
       scanf("%d",&a[a_i]);
    }
    
    for (int a0 = 0; a0 < q; a0++) 
    {
        int m; 
        scanf("%d",&m);
        
        if (k <= m) {
            (void)printf("%d\n", a[m - k]);
        } else {
            (void)printf("%d\n", a[n + m - k]);
        }
    }
    
    return EXIT_SUCCESS;
}
