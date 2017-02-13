#include <stdlib.h>
#include <limits.h>

int intCompare(const void *left, const void *right) 
{
    const int leftVal  = *((const int*)left);
    const int rightVal = *((const int*)right);
    
    if (rightVal > leftVal) {
        return 1;
    }
    else if(leftVal > rightVal) {
        return -1;
    }
    
    return 0;
}

int majorityElement(int* nums, int numsSize) 
{
    if (numsSize == 0) {
        return INT_MIN;
    }
    
    qsort(nums, numsSize, sizeof(*nums), intCompare);
    
    int count = 1;
    
    for (int index = 1; index <= numsSize; ++index) 
    {
        if (index == numsSize || count > numsSize / 2) {
            return nums[index - 1];
        }
        
        if (nums[index - 1] == nums[index]) {
            ++count;
        } else {
            count = 1;
        }
    }
    
    return INT_MIN;
}
