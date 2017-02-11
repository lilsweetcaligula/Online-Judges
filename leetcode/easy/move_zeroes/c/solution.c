/*
 * Slow/fast pointer solution, reminiscent of the Lomuto partitioning
 * scheme:
 *  https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
 */

void moveZeroes(int* nums, int numsSize) 
{
    int slow = 0;
    
    for (int fast = 0; fast < numsSize; ++fast) {
        if (nums[fast] != 0) {
            nums[slow] = nums[fast];
            ++slow;
        }
    }
    
    while (slow < numsSize) {
        nums[slow++] = 0;
    }
}
