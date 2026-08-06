class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        cycle = 2 * (numRows - 1)
        
        zigzag = []

        for row in range(numRows):
            for i in range(row, len(s), cycle):
                zigzag.append(s[i])

                diagonal = i + cycle - 2 * row

                if row != 0 and row != numRows - 1 and diagonal < len(s):
                    zigzag.append(s[diagonal])

        return "".join(zigzag)
