class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MIN = -2 ** 31
        INT_MAX = 2 ** 31 - 1

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX 

        is_negative = (dividend < 0) ^ (divisor < 0)

        if 0 < dividend:
            dividend = -dividend

        if 0 < divisor:
            divisor = -divisor

        quotient = 0

        while dividend <= divisor:
            temp = divisor
            multiple = 1

            while (INT_MIN >> 1) <= temp and dividend <= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        return -quotient if is_negative else quotient
