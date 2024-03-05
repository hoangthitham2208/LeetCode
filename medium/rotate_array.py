class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        rotated_array = [0] * len(nums)

        for i in range(len(nums) - k):
            rotated_array[i + k] = nums[i]

        for i in range(k):
            rotated_array[i] = nums[len(nums) - k + i]

        nums[:] = rotated_array
