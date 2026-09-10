class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0

        while x != 0:
            digit = x % 10
            result = 10 * result + digit
            x //= 10
            
        result *= sign

        if result < -2**31 or result > 2**31 - 1:
            return 0
        else:
            return result 
