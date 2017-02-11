/*
 * A classic O(n) approach to the problem is the slow/fast pointer/index technique.
 * Walk the array with a fast index, if the fast and slow indices do not point to
 * a duplicate, copy the value to nums[slow + 1] from nums[fast].
 *
 * At the end of the pass, the size of the array will be slow + 1, which we return
 * as required.
 *
 */

int removeDuplicates(int* nums, int numsSize) 
{
    if (numsSize == 0) {
        return 0;
    }
    
    int slow = 0;
    int fast = 0;
    
    while (fast < numsSize) {
        if (nums[slow] != nums[fast]) {
            nums[++slow] = nums[fast];
        }
        ++fast;
    }
    
    return ++slow;
}
