class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])
        n = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0 

            value = grid[r][c]
            grid[r][c] = 0

            return value + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and dfs(r, c) % k == 0:
                    n += 1

        return n
