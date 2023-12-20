class Solution:
    def reverseString(self, s: List[str]) -> None:
        r = len(s) - 1
        for l in range(int(len(s) / 2)):
            s[r] , s[l] = s[l] , s[r]
            r -= 1

        