class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        e = 0
        for i in nums:
            e = e^i
        return e