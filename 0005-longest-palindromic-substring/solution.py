class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "🍆💦" + "💦".join(s) + "💦🍑"
        n = len(t)
        lengths = [0] * n

        center = 0
        right = 0

        for i in range(1, n - 1):
            j = 2 * center - i

            if i < right:
                lengths[i] = min(lengths[j], right - i)

            while t[i - 1 - lengths[i]] == t[i + 1 + lengths[i]]:
                lengths[i] += 1

            if i + lengths[i] > right:
                center = i
                right = i + lengths[i]

        max_length, center_index = max((val, idx) for idx, val in enumerate(lengths))

        start = (center_index - max_length) // 2

        return s[start : start + max_length]
