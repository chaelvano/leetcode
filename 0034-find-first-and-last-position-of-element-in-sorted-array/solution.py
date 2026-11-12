class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)

        low = 0
        high = n

        while low < high:
            mid = (low + high) // 2

            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid

        left = low

        low = 0
        high = n

        while low < high:
            mid = (low + high) // 2

            if target < nums[mid]:
                high = mid
            else:
                low = mid + 1

        right = low - 1

        return [-1, -1] if left > right else [left, right]
