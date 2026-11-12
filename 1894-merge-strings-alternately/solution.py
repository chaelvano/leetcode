class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        m = len(word1)
        n = len(word2)
        p1 = p2 = 0

        while p1 < m and p2 < n:
            res.append(word1[p1])
            res.append(word2[p2])

            p1 += 1
            p2 += 1

        if m < n:
            res.append(word2[m:])
        else:
            res.append(word1[n:])

        return "".join(res)
