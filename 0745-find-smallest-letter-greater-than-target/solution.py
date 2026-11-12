class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        low = 0
        n = high = len(letters)

        while low < high:
            mid = (low + high) // 2

            if target < letters[mid]:
                high = mid
            else:
                low = mid + 1

        return letters[low % n]
