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
    
    int arr[n];
    for(int arr_i = 0; arr_i < n; arr_i++){
       scanf("%d",&arr[arr_i]);
    }
    
    long long llsum = 0LL;
    for (int i = 0; i < n; ++i) {
        llsum += arr[i];
    }
    
    printf("%lld\n", llsum);
    
    return 0;
}
