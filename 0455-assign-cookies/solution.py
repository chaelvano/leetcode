class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()

        n_children = len(g)
        n_cookies = len(s)
        
        count = 0
        child = 0
        cookie = 0

        while child < n_children and cookie < n_cookies:
            if g[child] <= s[cookie]:
                count += 1
                child += 1
                cookie += 1
            else:
                cookie += 1

        return count
