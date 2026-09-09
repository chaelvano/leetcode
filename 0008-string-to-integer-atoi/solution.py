class Solution:
    def myAtoi(self, s: str) -> int:
        LOWER_LIMIT = -2**31
        UPPER_LIMIT = 2**31 - 1

        sign = 1
        result = 0
        start = 0

        while start < len(s) and s[start] == " ":
            start += 1
        
        if start >= len(s):
            return 0

        if s[start] == "+":
            start += 1
        elif s[start] == "-":
            sign = -1

            start += 1

        for i in range(start, len(s)):
            if not s[i].isdigit():
                break

            result = 10 * result + int(s[i])

        result = sign * result

        if result < LOWER_LIMIT:
            return LOWER_LIMIT

        if result > UPPER_LIMIT:
            return UPPER_LIMIT

        return result
            

