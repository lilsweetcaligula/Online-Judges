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
    
    const double UNIT_RATIO = 1.0 / n;
    
    double posratio = 0.0;
    double negratio = 0.0;
    double zratio   = 0.0;
    
    int value = 0;    
    
    for (int i = 0; i < n; ++i) {
        value = arr[i];
        if (value > 0) {
            posratio += UNIT_RATIO;
        } else if (value < 0) {
            negratio += UNIT_RATIO;
        } else {
            zratio += UNIT_RATIO;
        }
    }
    
    printf("%lf\n", posratio);
    printf("%lf\n", negratio);
    printf("%lf\n", zratio);
    
    return 0;
}
