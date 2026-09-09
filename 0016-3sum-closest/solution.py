class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        length = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(length - 2):
            if i > target and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = length - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                distance = target - total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

                if abs(distance) < abs(target - closest):
                    closest = total

        return closest
