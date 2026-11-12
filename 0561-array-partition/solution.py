class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        maximized_sum = 0

        for i in range(0, len(nums), 2):
            maximized_sum += nums[i]

        return maximized_sum
