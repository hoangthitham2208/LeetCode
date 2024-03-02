class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_sorted = nums.sort()
        missing_pos = 1

        for i in nums:
            if (i == missing_pos):
                missing_pos+=1
            elif (i > missing_pos):
                return missing_pos

        return missing_pos