class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        number = 0

        for byte in columnTitle.encode():
            number = number * 26 + byte - 64

        return number
