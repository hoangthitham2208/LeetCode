class Solution:
    def findMin(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        return sorted_nums[0]
