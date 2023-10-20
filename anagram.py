class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [*s]
        t = [*t]
        if len(s) != len(t):
            return False
        for i in s:
            if i not in t:
                return False
            else:
                t.remove(i)
        return True
        
