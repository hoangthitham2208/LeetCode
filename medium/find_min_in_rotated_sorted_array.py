class Solution:
    def findMin(self, nums: List[int]) -> int:
        sort = sorted(nums)
        return sort[0]
