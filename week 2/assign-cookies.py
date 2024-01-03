class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        child = 0
        cookie = 0
        count = 0

        g.sort()
        s.sort()

        while child < len(g) and cookie < len(s):
            if g[child] <= s[cookie]:
                count += 1
                child += 1
            cookie += 1
        return count
        
        