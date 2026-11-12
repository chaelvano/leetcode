class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0

        for char in set(s):
            count = s.count(char)

            length += count if count % 2 == 0 else count - 1

        return length if length == len(s) else length + 1
