class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        right = len(s) - 1

        while s[right] == " ":
            right -= 1

        while right >= 0 and s[right] != " ":
            length += 1
            right -= 1

        return length
