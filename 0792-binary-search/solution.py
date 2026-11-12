class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)

        while low < high:
            mid = (low + high) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid
            else:
                low = mid + 1

        return -1
