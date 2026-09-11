class Solution:
    def mySqrt(self, x: int) -> int:
        y = 0
        left = 1
        right = x

        while left <= right:
            mid = left + (right - left) // 2

            if mid <= x // mid:
                y = mid
                left = mid + 1
            else:
                right = mid - 1

        return y
