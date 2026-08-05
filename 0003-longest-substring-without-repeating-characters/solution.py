class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}

        length = 0
        left = 0
        
        for right, char in enumerate(s):
            if char in map and map[char] >= left:
                left = map[char] + 1

            map[char] = right
            length = max(length, right - left + 1)

        return length

