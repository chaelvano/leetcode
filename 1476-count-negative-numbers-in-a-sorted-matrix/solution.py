class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        count = 0

        if m > n:
            for col in range(n):
                high = 0
                low = m

                while low > high:
                    mid = (low + high) // 2

                    if 0 > grid[mid][col]:
                        low = mid
                    else:
                        high = mid + 1

                count += m - high
        else:
            for row in range(m):
                high = 0
                low = n

                while low > high:
                    mid = (low + high) // 2

                    if 0 > grid[row][mid]:
                        low = mid
                    else:
                        high = mid + 1

                count += n - high

        return count

