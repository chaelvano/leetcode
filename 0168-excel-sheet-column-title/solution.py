class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        title = []

        append = title.append   # avoid repeated attribute lookup

        while columnNumber:
            columnNumber, remainder = divmod(columnNumber - 1, 26)

            append(letters[remainder])

        return "".join(reversed(title))
