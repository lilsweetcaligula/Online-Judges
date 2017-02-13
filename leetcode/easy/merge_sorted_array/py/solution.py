class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        result = []        
        i = 0
        j = 0
        
        for k in range(m + n):
            
            if i >= m and j < n:
                result.append(nums2[j])
                j += 1
                
            elif j >= n:
                result.append(nums1[i])
                i += 1
                
            elif nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
                
            else:
                result.append(nums2[j])
                j += 1
                
        nums1[:] = result
