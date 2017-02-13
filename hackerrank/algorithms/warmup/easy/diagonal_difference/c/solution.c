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
    
    int a[n][n];
    for(int a_i = 0; a_i < n; a_i++) {
       for(int a_j = 0; a_j < n; a_j++) {
          scanf("%d",&a[a_i][a_j]);
       }
    }
    
    int sum1 = 0, sum2 = 0;
    for (int a_i = 0; a_i < n; a_i++) {
        for (int a_j = 0; a_j < n; a_j++) {
            if (a_i == a_j) sum1 += a[a_i][a_j];
            if (a_j + a_i == n - 1) sum2 += a[a_i][a_j];
        }
    }
    
    int diff = abs(sum2 - sum1);
    printf("%d\n", diff);
    
    return 0;
}
