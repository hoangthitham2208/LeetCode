class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.findFirst(nums, target)
        end = self.findLast(nums, target)

        if start > end:
            return [-1, -1]

        return [start, end]

    def findFirst(self, nums, target):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] == target:
                result = mid

        return result

    def findLast(self, nums, target):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

            if nums[mid] == target:
                result = mid

        return result
