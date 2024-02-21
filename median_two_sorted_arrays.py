class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_sorted = sorted(nums1+nums2)
        length = len(merged_sorted)

        if length%2==1:
            return merged_sorted[(length//2)]
        else:
            right = length//2
            left = right-1
            return (merged_sorted[right]+merged_sorted[left])/2
