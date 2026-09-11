class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def ways(step):
            if step == 1: return 1
            if step == 2: return 2
            if step in memo: return memo[step]

            memo[step] = ways(step - 2) + ways(step - 1)

            return memo[step]

        return ways(n)
