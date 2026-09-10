class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(open, closed, s):
            if open == closed == n:
                result.append(s)

                return

            if open < n:
                backtrack(open + 1, closed, s + "(")

            if closed < open:
                backtrack(open, closed + 1, s + ")")

        backtrack(0, 0, "")

        return result
