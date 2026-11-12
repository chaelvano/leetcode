class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        m = n = i = -1

        for idx, val in enumerate(nums):
            if val > m:
                n = m
                m = val
                i = idx
            elif val > n:
                n = val

        return i if m >= 2 * n else -1

