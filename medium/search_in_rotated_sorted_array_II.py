class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        list = set(nums)
        if target in list:
            return True
        return False
