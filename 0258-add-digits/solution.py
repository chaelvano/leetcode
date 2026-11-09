class Solution:
    def addDigits(self, num: int) -> int:
        if num // 10 < 1:
            return num

        total = 0

        while num > 0:
            remainder = num % 10
            num -= remainder

            total += remainder
            num /= 10

        return self.addDigits(int(total))
