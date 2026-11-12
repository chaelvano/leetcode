class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        l = len(flowerbed)

        for i in range(l):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i - 1] == 0) and (i == l - 1 or flowerbed[i + 1] == 0):
                    flowerbed[i] = 1

                    n -= 1

            if n <= 0:
                return True

        return False
