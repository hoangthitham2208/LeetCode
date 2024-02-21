<<<<<<< HEAD
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
=======
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
>>>>>>> 790af3fb5457fb6b1af5ab4e1673a42d6cd11c56
