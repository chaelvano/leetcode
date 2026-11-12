class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        n = len(bits) - 1
        i = 0

        while i < n:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return i == n
