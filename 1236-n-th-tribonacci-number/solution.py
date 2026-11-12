class Solution:
    memo = {
        0: 0,
        1: 1,
        2: 1
    }

    def tribonacci(self, n: int) -> int:
        if n in Solution.memo:
            return Solution.memo[n]
        else:
            Solution.memo[n] = self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)

            return Solution.memo[n]
