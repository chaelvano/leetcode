class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        ranges = []
        n = len(nums)

        if n == 0:
            return ranges

        left = 0
        right = 1

        while right < n:
            if nums[right] - nums[right - 1] != 1:
                if right - left == 1:
                    ranges.append(f"{nums[left]}")
                else:
                    ranges.append(f"{nums[left]}->{nums[right - 1]}")
                
                left = right
                right += 1
            else:
                right += 1

        if right - left == 1:
            ranges.append(f"{nums[left]}")
        else:
            ranges.append(f"{nums[left]}->{nums[right - 1]}")

        return ranges
