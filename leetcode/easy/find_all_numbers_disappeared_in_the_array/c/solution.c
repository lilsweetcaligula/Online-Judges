#include <stdlib.h>

int compareIntegers(const int *lhs, const int *rhs) {
    return *lhs - *rhs;
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize) {
    const int startValue = 1;
    const int endValue   = numsSize;

    *returnSize = 0;
    int *buffer = (int*)malloc(sizeof(nums[0]) * numsSize);
    if (buffer)
    {
        // Sort the array to group up the duplicates.
        qsort(nums, numsSize, sizeof(nums[0]), compareIntegers);
        
        for (int index = 0, value = startValue; value <= endValue; ++value) 
        {
            // If we are faced with a duplicate, simply ignore it, and move 
            // a step forward.
            if (index > 0 && nums[index] == nums[index - 1]) {
                ++index;
            }
            
            // Here we should run into a number which is equal to the value.
            // If not, the value is not in the array, hence classified as one
            // of the "disappeared" numbers.
            if (nums[index] != value) {
                buffer[(*returnSize)++] = value;
            } else {
                ++index;
            }
        }
    }
    return buffer;
}
