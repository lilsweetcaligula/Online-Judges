#include <stdlib.h>
#include <math.h>

#define MIN(a, b) (((a) < (b)) ? (a) : (b))

int compareIntegers(const int *lhs, const int *rhs) {
    return *lhs - *rhs;
}

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* intersection(
    int* nums1, int nums1Size, 
    int* nums2, int nums2Size, 
    int* returnSize) 
{
    // Zero out the return size. Obvious, but easy to overlook.
    *returnSize = 0;

    // The largest possible size of the intersection is the size of the
    // smallest array. This is because whatever extra values the largest
    // array has, there can physically be no intersection.
    int *buffer = (int*)malloc(sizeof(nums1[0]) * MIN(nums1Size, nums2Size));
    
    if (buffer) 
    {
        // Make sure buffer allocation was successful. If it wasn't, this block
        // will be skipped and NULL returned from the function.
    
        // Sort both arrays to put numbers in both arrays in the order relative
        // to each other.        
        qsort(nums1, nums1Size, sizeof(nums1[0]), compareIntegers);
        qsort(nums2, nums2Size, sizeof(nums2[0]), compareIntegers);
        
        int i = 0; 
        int j = 0;
        
        while (i < nums1Size && j < nums2Size) 
        {            
            if (nums1[i] < nums2[j]) {
                // Value in the first array smaller than the one in the second?
                // We are falling behind in the first array, move the first array's
                // index forward.
                ++i;                
            } else if (nums1[i] > nums2[j]) {
                // Ditto, except now we are falling behind in the second array. Move
                // the second array's index forward.
                ++j;                
            } else if (i + 1 < nums1Size && nums1[i] == nums1[i + 1]) {
                // We've reached our intersection, but there are duplicates ahead
                // in the first array. The spec requires that there be no duplicates
                // in the result.
                ++i;
            } else if (j + 1 < nums2Size && nums2[j] == nums2[j + 1]) {
                // Ditto, except now there are duplicates in the second array.
                ++j;
            } else {
                // No duplicates ahead in eithe array, intersection. Store the value
                // in the buffer and increment its size.
                buffer[(*returnSize)++] = nums1[i];
                ++i; ++j;
            }            
        }
    }
    
    return buffer;
}
